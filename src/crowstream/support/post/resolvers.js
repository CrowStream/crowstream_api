import {generalRequest, getRequest} from '../../../utilities';
import {url, port} from '../server';

const URL = `http://${url}:${port}/posts`;

//const WAI = `http://localhost:3000/whoAmI`;

const resolvers = {
    Query: {
        retrieveAllPost: (_) => {
            return getRequest(URL, '');
        },
        retrievePostByID: (_, id_post) => {
            return getRequest(URL, id_post.id_post);
        }
    },
    Mutation: {
        createPost: (_, post) => {
            return generalRequest(URL, 'POST', post.post);
        },
        updatePost: (_, id_post, post) => {
            return generalRequest(`${URL}/${id_post.id_post}`, 'PUT', post.post);
        },
        deletePost: (_, id_post) => {
            return generalRequest(`${URL}/${id_post.id_post}`, 'DELETE');
        }
    }
}

export default resolvers;