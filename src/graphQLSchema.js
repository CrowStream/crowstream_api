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
	postMutations,
	postQueries,
	postTypeDef 
} from './crowstream/support/post/typeDefs';
import postResolvers from './crowstream/support/post/resolvers';
import { 
	supportRequestMutations,
	supportRequestQueries, 
	supportRequestTypeDef 
} from './crowstream/support/support_request/typeDefs';
import supportRequestResolvers from  './crowstream/support/support_request/resolvers';

// merge the typeDefs
const mergedTypeDefs = mergeSchemas(
	[
		'scalar JSON',
		accountTypeDef,
		profileTypeDef,
		postTypeDef,
		supportRequestTypeDef
	],
	[
		accountQueries,
		profileQueries,
		postQueries,
		supportRequestQueries
	],
	[
		accountMutations,
		profileMutations,
		postMutations,
		supportRequestMutations
	]
);

// Generate the schema object from your types definition.
export default makeExecutableSchema({
	typeDefs: mergedTypeDefs,
	resolvers: merge(
		{ JSON: GraphQLJSON }, // allows scalar JSON
		accountResolvers,
		profileResolvers,
		postResolvers,
		supportRequestResolvers
	)
});
