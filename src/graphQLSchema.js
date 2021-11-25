import merge from 'lodash.merge';
import GraphQLJSON from 'graphql-type-json';
import {makeExecutableSchema} from 'graphql-tools';

import {mergeSchemas} from './utilities';

import {
	categoryMutations,
	categoryQueries,
	categoryTypeDef
} from './supermarket/categories/typeDefs';
import categoryResolvers from './supermarket/categories/resolvers';

import {
	accountMutations,
	accountQueries,
	accountTypeDef
} from './crowstream/user/account/typeDefs';
import accountResolvers from './crowstream/user/account/resolvers';

// merge the typeDefs
const mergedTypeDefs = mergeSchemas(
	[
		'scalar JSON',
		categoryTypeDef,
		accountTypeDef
	],
	[
		categoryQueries,
		accountQueries
	],
	[
		categoryMutations,
		accountMutations
	]
);

// Generate the schema object from your types definition.
export default makeExecutableSchema({
	typeDefs: mergedTypeDefs,
	resolvers: merge(
		{ JSON: GraphQLJSON }, // allows scalar JSON
		categoryResolvers,
		accountResolvers
	)
});
