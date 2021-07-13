import mongoose, { Model } from 'mongoose';
import { UserFormQuestionsModel } from '../interface/UserFormQuestionsModel';

const schema = new mongoose.Schema(
  {
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
