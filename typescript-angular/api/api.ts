export * from './company.service';
import { CompanyService } from './company.service';
export * from './cyclo.service';
import { CycloService } from './cyclo.service';
export * from './facility.service';
import { FacilityService } from './facility.service';
export const APIS = [CompanyService, CycloService, FacilityService];
