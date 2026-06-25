const { Kafka } = require("kafkajs");

// para executar localmente
const IS_LOCAL = process.env.ICEF_KAFKA_IS_LOCAL === "true" || false;



//configuração do kafka
const kafka = new Kafka({
  clinetId: "icef-fun-evento-trigger",
  brokers: [process.env.ICEF_KAFKA_SERVER],
  ssl: !IS_LOCAL,
  sasl: !IS_LOCAL
    ? {
        mechanism: "plain",
        username: process.env.ICEF_KAFKA_CLUSTER_API_KEY,
        password: process.env.ICEF_KAFKA_CLUSTER_API_PASSWORD,
      }
    : undefined,
});

const topic = process.env.ICEF_KAFKA_TOPIC_RECPARQUIVOS;

export const producer = kafka.producer({
  batch: {
    size: 16384, //tamanho maximo de bytes de um lote
    maxWaitTime: 1, //tempo maximo de espera em ms para enviar um lote
  },
  maxBlockTime: 5000, //tempo maximo de bloqueio em ms
  bufferMemory: 33554432, //tamanho maximo de buffer em bytes,mensssagens na memoria
  retry: {
    initialRetryTime: 3000, //tempo inicial de espera entre tentativa 3 segundos
    maxRetryTime: 30000, //tempo maximo de espera entre tentativa 30 segundos
    retries: 7, // em caso de falha ele tentara enviar a mensagem 10 vezes
    factor: 2,//fator exponencial para mutiplicação do tempo nas tentativas
  },
});

//conectar com o kafka
export async function producerStart() {
  try {
    await producer.connect();
    console.log("Connected successfully");
  } catch (e) {
    console.error("Error connecting producer:", e);
  }
}

//produzir mensagem
export async function producerSend(idTransacao:string,centroCusto:string,data:string,files: string[]) {
  await producerStart();

  try {
    const res = [];   

    res.push(
      producer.send({
        acks: -1, // todas as replicas (brokers) devem confirmar o recebimento da mensagem
        topic: topic,
        messages: [
          {
            headers: {
              idTransacao: idTransacao,
              centroDeCusto: centroCusto,
              date: data
            },
            value: JSON.stringify({"nomeArquivo": files})
          },
        ],
      })
    );

    await Promise.all(res);
    console.log("Mensagem enviada com sucesso...");
    return true;
  } catch (er) {
    console.error("Erro ao enviar a mensagem", er);
    return false;
  } finally {
    await producerDisconnect()
  }

  
}

//desconectar do kafka
export async function producerDisconnect() {
  await producer.disconnect();
  console.log("Disconnected successfully");
}
