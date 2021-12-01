export const userVideoMetadataTypeDef = `
  type UserVideoMetadata {
      ID: ID!
      user_id: Int!
      video_id: Int!
      video_progress: Float!
      video_progress_time: String!
  }
  input UserVideoMetadataInput {
      user_id: Int!
      video_id: Int!
      video_progress: Float!
      video_progress_time: String!
  }`;

export const userVideoMetadataQueries = `
      userVideoMetadataById(id: Int!): UserVideoMetadata!
  `;

export const userVideoMetadataMutations = `
    createUserVideoMetadata(userVideoMetadata: UserVideoMetadataInput!): UserVideoMetadata!
`;