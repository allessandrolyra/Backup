import { Claims, TokenIssuer, } from "@bradesco/enge-lib-js-token-issuer";
import { cleanCertDirectory, geraCertificado } from "./certificateService";
import * as crypto from 'crypto';

export async function getToken(): Promise<string> {
    try {
        const frwk: any = {
        };

        const secondsToExpire = 1800;
        const expiration = Math.floor(Date.now() / 1000) + secondsToExpire;
        const idAcesso = crypto.randomBytes(8).toString('hex');
        const claim = new Claims("brai", "brai", expiration, idAcesso, frwk, "CPF#00000000000");

        const certPath = await geraCertificado();
        const issuer = new TokenIssuer(certPath, "funcazudvbracdconsigprivconc");
        // Limpando diretorio TEMP '/certs'
        cleanCertDirectory();

        const token = await issuer.generateToken(claim)
        console.log("Token gerado com sucesso!: ", token);
        return token;
    } catch (error) {
        console.error("ERRO: Não foi possivel gerar o Token: ", error)
        throw new Error('Falha ao gerar o token.');
    }
}