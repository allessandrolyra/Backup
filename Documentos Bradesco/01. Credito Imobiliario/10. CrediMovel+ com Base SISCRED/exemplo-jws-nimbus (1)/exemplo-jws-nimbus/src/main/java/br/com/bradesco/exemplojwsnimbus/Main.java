package br.com.bradesco.exemplojwsnimbus;

import com.nimbusds.jose.JOSEException;
import com.nimbusds.jose.JWSAlgorithm;
import com.nimbusds.jose.JWSHeader;
import com.nimbusds.jose.JWSObject;
import com.nimbusds.jose.Payload;
import com.nimbusds.jose.crypto.RSASSASigner;
import com.nimbusds.jose.crypto.bc.BouncyCastleProviderSingleton;
import com.nimbusds.jose.jwk.JWK;
import com.nimbusds.jose.jwk.JWKSet;
import com.nimbusds.jose.jwk.RSAKey;
import com.nimbusds.jose.util.X509CertUtils;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.cert.X509Certificate;
import java.security.interfaces.RSAPrivateKey;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

public class Main {

  public static void main(String... args) throws JOSEException, IOException {
    //Prepara Claims
    Map<String, Object> claims = new HashMap<>();
    claims.put("aud", "bcpf");
    claims.put("sub", "cartoesapp");
    claims.put("scope", "bcpf");
    claims.put("iss", "cartoes");
    claims.put("exp", new Date(new Date().getTime() + 30 * 1000)); //30 minutos
    claims.put("iat", new Date().getTime()); //agora
    claims.put("jti", "tITZMoelE0/BY8ik1Jxyyg");
    claims.put("idAcesso", "12ajk1lh2");

    //Prepara JWS
    JWSObject jws = new JWSObject(new JWSHeader.Builder(JWSAlgorithm.PS256).keyID(
        getCertificado().getSerialNumber().toString()).build(),
        new Payload(claims));

    //Prepara signer
    RSASSASigner signer = new RSASSASigner(getChavePrivada());

    //Setta o bouncycastle como provedor (isso possibilitará usar algorítmos como PS256 em versões antigas de java)
    signer.getJCAContext().setProvider(BouncyCastleProviderSingleton.getInstance());

    //Assina token
    jws.sign(signer);

    //Serializa token
    String jwsSerializado = jws.serialize();

    //Usa token
    System.out.println(jwsSerializado);

    //Obtém JWKS (para informar à equipe de API Estrutural)
    JWKSet jwkSet = new JWKSet(JWK.parse(getCertificado()));
    System.out.println(jwkSet.toPublicJWKSet().toJSONObject());
  }

  private static X509Certificate getCertificado() throws IOException {
    return X509CertUtils.parse(leArquivo("src/main/resources/mycert.pem"));
  }

  private static RSAPrivateKey getChavePrivada() throws JOSEException, IOException {
    return RSAKey.parseFromPEMEncodedObjects(leArquivo("src/main/resources/mycert.pem")).toRSAKey()
        .toRSAPrivateKey();
  }

  private static String leArquivo(String path) throws IOException {
    return new String(Files.readAllBytes(Paths.get(path)));
  }
}
