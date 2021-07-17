import { UserFormQuestions } from '../dtos/UserFormQuestions';
import { Document } from 'mongoose';

export interface UserFormQuestionsModel
  extends Omit<UserFormQuestions, '_id'>,
    Document {}
