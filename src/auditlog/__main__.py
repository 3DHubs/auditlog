from argparse import ArgumentParser
from datetime import datetime
from uuid import uuid4

from .models import AuditEvent, Session, Identity


if __name__ == "__main__":
    ap = ArgumentParser()
    ap.add_argument("generate", choices=["schema", "example"], help="Generate a schema or event sample")
    args = ap.parse_args()

    ev = AuditEvent(
            timestamp=datetime.now(),
            id=str(uuid4()),
            name="SampleEvent",
            description="An example auditable event",
            source="org.orderservice",
            attributes=dict(resource="order", action="ManualPriceUpdate"),
            identity=Identity(
                id=str(uuid4()),
                name="marvin@example.com",
                issuer="org.sso.okta",
                session=Session(
                    id=str(uuid4()),
                    issued_at=datetime.now(),
                    issuer="org.identityservice",
                    attributes=dict(roles=["customer_support", "order_manager"]),
                ),
            ),
    )

    match args.generate:
        case "schema":
            print(ev.schema_json(indent=2))
        case "example":
            print(ev.json())
