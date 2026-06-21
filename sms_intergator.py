
from typing import Protocol


class PFPortal(Protocol):
    def deduct_pf(self, employee_id: str, amount: float) -> None:
        ...

class MockPFPortal1:
    def deduct_pf(self, employee_id: str, amount: float) -> None:
        print(f"Mock deducting {amount} from PF for employee {employee_id} using PFPortal1.")

class MockPFPortal2:
    def send_pf_amount(self, employee_id: str, amount: float) -> None:
        print(f"Mock sending {amount} to PF for employee {employee_id} using PFPortal2.")

class PFPortal1:
    def deduct_pf(self, employee_id: str, amount: float) -> None:
        print(f"Deducting {amount} from PF for employee {employee_id} using PFPortal1.")


class PFPortal2:
    def deduct_pf(self, employee_id: str, amount: float) -> None:
        print(f"Deducting {amount} from PF for employee {employee_id} using PFPortal2.")


class PFFactory:
    @staticmethod
    def create(portal_type: str) -> PFPortal:
        if portal_type == "v1":
            return PFPortal1()
        elif portal_type == "v2":
            return PFPortal2()
        else:
            raise ValueError(f"Unsupported PF portal type: {portal_type}")

import json
with open("C:\\KripaDev\\AIML_Batch_005\\design-patterns\\config.json") as f:
    config = json.load(f)

poratal_version = config.get("pfportal_version", "v1")

obj1 = PFFactory.create(poratal_version)
obj1.deduct_pf("E123", 1000.0)

obj2 = PFFactory.create(poratal_version)
obj2.deduct_pf("E456", 2000.0)