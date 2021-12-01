export const postTypeDef = `
    input PostInput {
        user_id: String!
        description: String!
        comments: [CommentInput]
        files: [String]
    }
    input CommentInput {
        user_id: String!
        description: String!
        files: [String]
    }
    type Post {
        _id: ID!
        user_id: String!
        description: String!
        comments: [Comment]
        files: [String]
    }
    type Comment {
        _id: ID!
        user_id: String!
        description: String!
        files: [String]
    }
`;

export const postQueries = `
    retrieveAllPost: [Post]!
    retrievePostByID(id_post: ID!): Post
`;

export const postMutations = `
    createPost(post: PostInput!): Post!
    updatePost(id_post: ID!, post: PostInput!): Post!
    deletePost(id_post: ID!): Boolean
`;