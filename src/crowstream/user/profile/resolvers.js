import {generalRequest, getRequest} from '../../../utilities';
import {url, port} from '../server';

const URL = `http://${url}:${port}/profiles`;

const resolvers = {
    Query: {
        allProfilesByUser: (_) =>
            getRequest(URL, ''),
        profileById: (_, { id }) =>
            generalRequest(`${URL}/${id}`, 'GET'),
    },
    Mutation: {
        createProfile: (_, profile) =>
            generalRequest(URL, 'POST', profile),
    }
}

export default resolvers;