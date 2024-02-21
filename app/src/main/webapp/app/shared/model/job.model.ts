import { ITask } from '@/shared/model/task.model';
import { IJobHistory } from '@/shared/model/job-history.model';
import { IEmployee } from '@/shared/model/employee.model';

export interface IJob {
  id?: number;
  jobTitle?: string | null;
  minSalary?: number | null;
  maxSalary?: number | null;
  tasks?: ITask[] | null;
  jobHistory?: IJobHistory | null;
  employee?: IEmployee | null;
}

export class Job implements IJob {
  constructor(
    public id?: number,
    public jobTitle?: string | null,
    public minSalary?: number | null,
    public maxSalary?: number | null,
    public tasks?: ITask[] | null,
    public jobHistory?: IJobHistory | null,
    public employee?: IEmployee | null
  ) {}
}
