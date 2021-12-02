import {generalRequest, getRequest} from '../../../utilities';
import {url, port} from '../server';

const URL = `http://${url}:${port}/posts`;

const WAI = `http://localhost:3000/whoAmI`;

const resolvers = {
    Query: {
        retrieveAllPost: (_) => {
            return getRequest(URL, '');
        },
        retrievePostByID: (_, data) => {
            return getRequest(URL, data.id_post);
        }
    },
    Mutation: {
        createPost: (_, data) => {
            return generalRequest(URL, 'POST', data.post);
        },
        updatePost: (_, data) => {
            return generalRequest(`${URL}/${data.id_post}`, 'PUT', data.post);
        },
        deletePost: (_, data) => {
            return generalRequest(`${URL}/${data.id_post}`, 'DELETE');
        },
        createComment: (_, data) => {
            return generalRequest(`${URL}/${data.id_post}/comments`, 'POST', data.comment);
        }
    }
}

export default resolvers;