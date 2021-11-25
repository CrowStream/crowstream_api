export const profileTypeDef = `
    type Profile {
        id: String!
        account_id: String
        name: String!
    }
    input ProfileInput {
        name: String!
    }
    type Profiles {
        account_id: String!
        profiles: [Profile]!
    }
`;

export const profileQueries = `
    allProfilesByUser: Profiles!
    profileById(id: String!): Profile!
`;

export const profileMutations = `
    createProfile(profile: ProfileInput!): Profile!
`;