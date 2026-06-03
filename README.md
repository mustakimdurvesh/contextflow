# ContextFlow 🌊

**Distributed Context Management Library** – Seamlessly propagate application context, metadata, tracing IDs, and feature flags across service boundaries, async operations, and execution contexts.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/typescript-5.0+-blue)](https://www.typescriptlang.org/)

## 🎯 What is ContextFlow?

ContextFlow is a lightweight, production-ready library inspired by OpenClaw's cross-context marker pattern. It provides:

- **📡 Cross-Context Propagation** – Pass metadata across HTTP, gRPC, message queues, and async tasks
- **🔌 Multiple Transport Adapters** – Headers, gRPC metadata, message queue payloads, custom transports
- **🎯 Scope Management** – Define context boundaries with clear parent-child relationships
- **🔐 Type-Safe Values** – Strongly-typed context keys and values
- **📊 Observability Integration** – Works seamlessly with OpenTelemetry
- **🚩 Feature Flag Support** – Built-in A/B testing and experimentation
- **🛡️ Security Context** – Propagate permissions, tokens, and user principals safely
- **🌍 Multi-Language Support** – Python, TypeScript (with Java, Go roadmap)

## 🚀 Quick Start

### Python

```bash
pip install contextflow
```

```python
from contextflow import ContextMarker, ContextScope

# Create a context marker
marker = ContextMarker()
marker.set('user_id', '12345')
marker.set('request_id', 'req-abc-def')
marker.set('feature_flag', 'new_ui_v2')

# Export for HTTP headers
headers = marker.to_headers()

# Import from incoming request
marker = ContextMarker.from_headers(request.headers)
user_id = marker.get('user_id')
```

### TypeScript

```bash
npm install @contextflow/core
```

```typescript
import { ContextMarker } from '@contextflow/core';

const marker = new ContextMarker();
marker.set('user_id', '12345');
marker.set('request_id', 'req-abc-def');
marker.set('feature_flag', 'new_ui_v2');

const headers = marker.toHeaders();
```

## 📚 Documentation

- [Getting Started Guide](./docs/getting-started.md)
- [API Reference](./docs/api-reference.md)
- [Integration Examples](./examples/)
- [Best Practices](./docs/best-practices.md)
- [Architecture](./docs/architecture.md)

## 🏗️ Architecture

```
ContextFlow
├── Core (Context Management)
│   ├── ContextMarker
│   ├── ContextScope
│   └── ContextRegistry
├── Transports (Data Format)
│   ├── HTTPHeaderTransport
│   ├── gRPCMetadataTransport
│   ├── MessageQueueTransport
│   └── CustomTransport
├── Integrations
│   ├── FastAPI
│   ├── Express
│   ├── Flask
│   └── Spring Boot
└── Observability
    └── OpenTelemetry Bridge
```

## 📖 Use Cases

✅ **Request Tracing** – Trace a single logical operation across multiple microservices  
✅ **Feature Flagging** – Consistently apply feature flags throughout request lifecycle  
✅ **Permission Propagation** – Pass user roles and permissions across service boundaries  
✅ **Correlation IDs** – Track related events for debugging and monitoring  
✅ **A/B Testing** – Distribute experiment assignments consistently  
✅ **Request-Scoped Config** – Share configuration without parameter passing  

## 📋 Roadmap

- [x] Core ContextMarker implementation
- [x] HTTP header transport
- [x] FastAPI integration
- [x] Express.js integration
- [x] Flask integration
- [ ] gRPC metadata transport
- [ ] Message queue transport (RabbitMQ, Kafka)
- [ ] OpenTelemetry integration
- [ ] Java SDK
- [ ] Go SDK
- [ ] Performance benchmarks
- [ ] Production examples

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License – see [LICENSE](./LICENSE) file

## 💬 Community

- GitHub Issues: [Report bugs](https://github.com/mustakimdurvesh/contextflow/issues)
- Discussions: [Join the conversation](https://github.com/mustakimdurvesh/contextflow/discussions)

---

**Context is king.** Start marking yours with ContextFlow today! 🚀
