import { IJob } from '@/shared/model/job.model';
import { IJobHistory } from '@/shared/model/job-history.model';
import { IDepartment } from '@/shared/model/department.model';

export interface IEmployee {
  id?: number;
  firstName?: string | null;
  lastName?: string | null;
  email?: string | null;
  phoneNumber?: string | null;
  hireDate?: Date | null;
  salary?: number | null;
  commissionPct?: number | null;
  jobs?: IJob[] | null;
  manager?: IEmployee | null;
  jobHistory?: IJobHistory | null;
  department?: IDepartment | null;
  employees?: IEmployee[] | null;
}

export class Employee implements IEmployee {
  constructor(
    public id?: number,
    public firstName?: string | null,
    public lastName?: string | null,
    public email?: string | null,
    public phoneNumber?: string | null,
    public hireDate?: Date | null,
    public salary?: number | null,
    public commissionPct?: number | null,
    public jobs?: IJob[] | null,
    public manager?: IEmployee | null,
    public jobHistory?: IJobHistory | null,
    public department?: IDepartment | null,
    public employees?: IEmployee[] | null
  ) {}
}
