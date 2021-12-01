import merge from 'lodash.merge';
import GraphQLJSON from 'graphql-type-json';
import {makeExecutableSchema} from 'graphql-tools';

import {mergeSchemas} from './utilities';

import {
	accountMutations,
	accountQueries,
	accountTypeDef
} from './crowstream/user/account/typeDefs';
import accountResolvers from './crowstream/user/account/resolvers';

import {
	profileMutations,
	profileQueries,
	profileTypeDef
} from './crowstream/user/profile/typeDefs';
import profileResolvers from './crowstream/user/profile/resolvers';

import {
	userVideoMetadataMutations,
	userVideoMetadataQueries,
	userVideoMetadataTypeDef
} from './crowstream/reproduction/typeDefs';
import userVideoMetadataResolvers from './crowstream/reproduction/resolvers';

// merge the typeDefs
const mergedTypeDefs = mergeSchemas(
	[
		'scalar JSON',
		accountTypeDef,
		profileTypeDef,
		userVideoMetadataTypeDef
	],
	[
		accountQueries,
		profileQueries,
		userVideoMetadataQueries
	],
	[
		accountMutations,
		profileMutations,
		userVideoMetadataMutations
	]
);

// Generate the schema object from your types definition.
export default makeExecutableSchema({
	typeDefs: mergedTypeDefs,
	resolvers: merge(
		{ JSON: GraphQLJSON }, // allows scalar JSON
		accountResolvers,
		profileResolvers,
		userVideoMetadataResolvers
	)
});
