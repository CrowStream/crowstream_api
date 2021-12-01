import {generalRequest, getRequest} from '../../../utilities';
import {url, port} from '../server';

const URL = `http://${url}:${port}/support_request`;

//const WAI = `http://localhost:3000/whoAmI`;

const resolvers = {
    Query: {
        retrieveAllSupportRequest: (_) => {
            return getRequest(URL, '')
        },
        retrieveSupportRequestByID: (_, id_support_request) => {
            return getRequest(URL, id_support_request.id_support_request)
        }
    },
    Mutation: {
        createSupportRequest: (_, support_request) => {
            return generalRequest(URL, 'POST', support_request.support_request);
        },
        updateSupportRequest: (_, id_support_request, support_request) => {
            return generalRequest(`${URL}/${id_support_request.id_support_request}`, 'PUT', support_request.support_request);
        },
        deleteSupportRequest: (_, id_support_request) => {
            return generalRequest(`${URL}/${id_support_request.id_support_request}`, 'DELETE');
        }
    }
}

export default resolvers;