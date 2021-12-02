import {generalRequest, getRequest} from '../../../utilities';
import {url, port} from '../server';

const URL = `http://${url}:${port}/support_requests`;

const WAI = `http://localhost:3000/whoAmI`;

const resolvers = {
    Query: {
        retrieveAllSupportRequest: (_) => {
            return getRequest(URL, '')
        },
        retrieveSupportRequestByID: (_, data) => {
            return getRequest(URL, data.id_support_request)
        }
    },
    Mutation: {
        createSupportRequest: (_, data) => {
            return generalRequest(URL, 'POST', data.support_request);
        },
        updateSupportRequest: (_, data) => {
            return generalRequest(`${URL}/${data.id_support_request}`, 'PUT', data.support_request);
        },
        deleteSupportRequest: (_, data) => {
            return generalRequest(`${URL}/${data.id_support_request}`, 'DELETE');
        }
    }
}

export default resolvers;