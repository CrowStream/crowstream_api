import {generalRequest} from '../../../utilities';
import {url, port} from '../server';

const URL = `http://${url}:${port}`;

const resolvers = {
    Query: { },
    Mutation: {
        signin: (_, { accountCredentials }) =>
            generalRequest(`${URL}/account/signin`, 'POST', accountCredentials),
        signup: (_, { accountCredentials }) =>
            generalRequest(`${URL}/signup`, 'POST', accountCredentials),
    }
}

export default resolvers;