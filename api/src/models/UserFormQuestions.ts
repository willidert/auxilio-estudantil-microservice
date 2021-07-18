import mongoose, { Model } from 'mongoose';
import { UserFormQuestionsModel } from '../interface/UserFormQuestionsModel';

const schema = new mongoose.Schema(
  {
    questionOne: { type: String },
    questionTwo: { type: String },
    questionThree: { type: String },
    questionFour: { type: String },
    questionFive: { type: String },
    questionSix: { type: String },
    questionSeven: { type: String },
    questionEight: { type: String },
    questionNine: { type: String },
    questionTen: { type: String },
    questionEleven: { type: String },
    questionTwelve: { type: String },
    questionThirteen: { type: String },
    questionFourteen: { type: String },
    questionFifteen: { type: String },
    questionSixteen: { type: String },
    questionSeventeen: { type: String },
    questionEighteen: { type: String },
    questionNineteen: { type: String },
    questionTwenty: { type: String },
    questionTwentyOne: { type: String },
    questionTwentyTwo: { type: String },
    email: {
      type: String,
      required: true,
      unique: [true, 'Email must be unique'],
    },
  },
  {
    toJSON: {
      transform: (_, ret): void => {
        ret.id = ret._id;
        delete ret._id;
        delete ret.__v;
      },
    },
  }
);

export const UserFormQuestions: Model<UserFormQuestionsModel> = mongoose.model(
  'UserFormQuestions',
  schema
);
