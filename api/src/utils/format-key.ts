import { Request } from 'express';

export const formatKey = (req: Request) => {
  const { questionEight } = req.body;

  let total: string = '';

  for (const value in questionEight) {
    if (questionEight[value] != '') {
      total += `${questionEight[value]};`;
    }
  }

  req.body.questionEight = total;
};
