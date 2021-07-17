import { Router, Request, Response } from 'express';
import UserFormController from '../controller/UserFormController';

export const router = Router();

router.get('/', (req: Request, res: Response) => {
  UserFormController.index(req, res);
});

router.post('/', (req: Request, res: Response) =>
  UserFormController.create(req, res)
);
