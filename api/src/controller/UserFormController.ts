import { Request, Response } from 'express';
import { UserFormQuestions } from '../models/UserFormQuestions';
import { formatKey } from '../utils/format-key';

export class UserFormController {
  /**
   * rota que salva o e-mail e o form do aluno
   * @param req
   * @param res
   */
  async create(req: Request, res: Response) {
    formatKey(req);

    try {
      const userFormQuestions = new UserFormQuestions(req.body);
      await userFormQuestions.save();
    } catch (error) {
      console.error(error);
    }

    res.json({
      message: 'Hello World',
      ...req.body,
    });
  }

  /**
   * Rota para verificar se a APi está funcionando
   * @param req
   * @param res
   */
  async index(req: Request, res: Response) {
    res.json({
      message: 'API Working',
      ...req.body,
    });
  }
}

export default new UserFormController();
