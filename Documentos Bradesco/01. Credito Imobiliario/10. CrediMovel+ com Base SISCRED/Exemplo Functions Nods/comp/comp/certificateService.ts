import * as fs from 'fs';
import * as crypto from 'crypto';
import * as path from 'path';
import { getSecretValue } from './keyVaultService';

// Função para limpar o diretório '/certs'
export const cleanCertDirectory = () => {
    // Define o diretório 'certs' no mesmo nível do arquivo atual
    const certDir = path.join(__dirname, '..', 'certs');
    try {
        const files = fs.readdirSync(certDir);
        // Percorre todos os arquivos no diretório        
        files.forEach((file) => {
            const filePath = path.join(certDir, file);
            // Exclui o arquivo
            if (fs.statSync(filePath).isFile()) {
                fs.unlinkSync(filePath);
                console.log(`Certificado temporario excluído: ${filePath}`);
            }
        });
    } catch (error) {
        console.error('Erro ao limpar o diretório certs:', error);
        throw new Error('Falha  ao limpar o diretório certs.');
    }
};

export async function geraCertificado(): Promise<string> {
    try {
        const certString = (await getSecretValue("secret-tokenIssuer-consig-inss-mkt")).toString();

        // Define o diretório 'certs' no mesmo nível do arquivo atual
        const certDir = path.join(__dirname, '..', 'certs');

        // Garante que o diretório 'certs' exista
        if (!fs.existsSync(certDir)) {
            fs.mkdirSync(certDir, { recursive: true }); // recursive garante a criação de subdiretórios, se necessário
        }

        // Gera um nome único para o arquivo temporário
        const tempFileName = `cert_${crypto.randomBytes(8).toString('hex')}.pem`;
        const tempFilePath = path.join(certDir, tempFileName);

        // Escreve o conteúdo do certificado no arquivo temporário
        fs.writeFileSync(tempFilePath, certString);

        console.log(`Certificado temporário criado: ${tempFileName}`);
        return tempFilePath; // Retorna o caminho do arquivo temporário
    } catch (error) {
        console.error('Erro ao gerar o certificado:', error);
        throw new Error('Falha ao criar o arquivo temporário do certificado.');
    }
}
