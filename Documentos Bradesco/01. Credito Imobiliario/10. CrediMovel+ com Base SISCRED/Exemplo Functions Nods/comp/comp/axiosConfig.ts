import axios from "axios";
import { InvocationContext } from "@azure/functions";
import axiosRetry from "axios-retry";
import * as https from 'https';

export function configureAxios(context: InvocationContext) {
    const httpsAgent = new https.Agent({
        rejectUnauthorized: false,
    });

    axiosRetry(axios, {
        retries: 3,
        retryDelay: (retryCount) => retryCount * 1000,
        retryCondition: (error) => axiosRetry.isNetworkOrIdempotentRequestError(error) || error.response?.status >= 500,
        onRetry: (retryCount, error, requestConfig) => {
            context.log(`Tentativa ${retryCount} para a URL ${requestConfig.url} devido a: ${error.message}`);
        }
    });

    return { httpsAgent }
}