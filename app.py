import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Set up the tracer provider
resource = Resource(attributes={
    SERVICE_NAME: "example-service"
})

trace.set_tracer_provider(TracerProvider(resource=resource))

# Create an OTLP exporter
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

# Create a batch span processor and add the OTLP exporter to it
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Create a tracer
tracer = trace.get_tracer(__name__)

# Create a span
with tracer.start_as_current_span("example-span") as span:
    span.set_attribute("http.method", "GET")
    span.set_attribute("http.url", "http://example.com")
    span.add_event("Event: Received response")

    # Simulate some work
    time.sleep(2)

print("Tracing complete")
