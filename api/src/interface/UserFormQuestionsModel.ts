import { UserFormQuestions } from '../dtos/UserFormQuestions';

export interface UserFormQuestionsModel
  extends Omit<UserFormQuestions, '_id'>,
    Document {}
