export const accountTypeDef = `
    type Account {
        id: String!
        email: String!
        is_email_verified: Boolean
    }
    type Token {
        token: String!
    }
    input AccountCredentials {
        email: String!
        password: String!
    }
`;

export const accountQueries = ``;

export const accountMutations = `
    signin(accountCredentials: AccountCredentials!): Token!
    signup(accountCredentials: AccountCredentials!): Account!
`;