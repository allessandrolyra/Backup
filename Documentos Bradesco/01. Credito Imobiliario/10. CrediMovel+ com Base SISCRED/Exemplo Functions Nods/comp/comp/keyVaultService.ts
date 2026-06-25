import { DefaultAzureCredential } from "@azure/identity";
import { SecretClient } from "@azure/keyvault-secrets";

//IMPLEMENTAÇÃO DO KEYVAULT
export async function getSecretValue(secretName: string) {
    //CERTIFICADO MOCKADO PARA LOCAL
    if (process.env.Ambiente === "Local" && secretName === 'secret-tokenIssuer-consig-inss-mkt') {
        return ``; //CERTIFICADO EM STRING
    }
    // URL do Key Vault - substitua pelo seu URL do Key Vault
    const keyVaultUrl = process.env.KeyVaultURL;

    // Cria uma instância do cliente usando credenciais padrão
    const credential = new DefaultAzureCredential();
    const client = new SecretClient(keyVaultUrl, credential);

    try {
        // Busca o valor do segredo pelo nome
        const secret = await client.getSecret(secretName);
        return secret.value;
    } catch (error) {
        console.error("Erro ao buscar segredo:", error);
        throw error;
    }
}
//IMPLEMENTAÇÃO DO KEYVAULT

