import { generalRequest, getRequest } from '../../utilities';
import { url, port, entryPoint } from './server';

const URL = `http://${url}:${port}/${entryPoint}`;

const resolvers = {
	Query: {
		userVideoMetadataById: (_, { id }) =>
			generalRequest(`${URL}/${id}`, 'GET'),
	},
	Mutation: {
		createUserVideoMetadata: (_, { userVideoMetadata }) =>
			generalRequest(`${URL}`, 'POST', userVideoMetadata),
	}
};

export default resolvers;