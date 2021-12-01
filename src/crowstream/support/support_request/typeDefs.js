export const supportRequestTypeDef = `
input SupportResponseInput {
    responder: String!
    description: String!
    files: [String]
}
input SupportRequestInput {
    user_id: String!
    request_type: String!
    description: String!
    response: [SupportResponseInput]
    files: [String]
}
type SupportRequest {
    _id: ID!
    user_id: String!
    request_type: String!
    description: String!
    response: [SupportResponse]
    files: [String]
}
type SupportResponse {
    _id: ID!
    responder: String!
    description: String!
    files: [String]
}
`;

export const supportRequestQueries = `
    retrieveAllSupportRequest: [SupportRequest]!
    retrieveSupportRequestByID(id_support_request: ID!): SupportRequest
`;

export const supportRequestMutations = `
    createSupportRequest(support_request: SupportRequestInput!): SupportRequest!
    updateSupportRequest(id_support_request: ID!, support_request: SupportRequestInput!): SupportRequest!
    deleteSupportRequest(id_support_request: ID!): Boolean
`;