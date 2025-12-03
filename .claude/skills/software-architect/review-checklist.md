# Architecture Review Checklist

Use this checklist when reviewing code or architecture from a software architect perspective.

## Code Structure & Organization

### Modularity
- [ ] Code is organized into logical modules/packages
- [ ] Clear boundaries between components
- [ ] Minimal coupling between modules
- [ ] High cohesion within modules
- [ ] Shared code is properly extracted to common utilities

### Separation of Concerns
- [ ] Business logic separated from infrastructure
- [ ] Presentation layer separated from business logic
- [ ] Data access abstracted behind interfaces
- [ ] Cross-cutting concerns (logging, auth) properly handled
- [ ] No mixed responsibilities within components

## SOLID Principles

### Single Responsibility
- [ ] Each class/module has one reason to change
- [ ] Functions do one thing well
- [ ] No "God objects" or oversized classes

### Open/Closed
- [ ] Open for extension, closed for modification
- [ ] Uses inheritance/composition appropriately
- [ ] Strategy pattern where algorithms vary
- [ ] Plugin architecture where needed

### Liskov Substitution
- [ ] Derived classes properly substitute base classes
- [ ] No breaking changes in inherited behavior
- [ ] Interface contracts are honored

### Interface Segregation
- [ ] Interfaces are focused and minimal
- [ ] Clients not forced to depend on unused methods
- [ ] Role-based interface design

### Dependency Inversion
- [ ] High-level modules don't depend on low-level modules
- [ ] Both depend on abstractions
- [ ] Abstractions don't depend on details
- [ ] Dependency injection used appropriately

## Design Patterns

### Pattern Usage
- [ ] Appropriate patterns applied (not over-engineered)
- [ ] Patterns solve actual problems
- [ ] Team understands patterns used
- [ ] Patterns documented in code/comments

### Anti-Patterns
- [ ] No God objects
- [ ] No circular dependencies
- [ ] No tight coupling to frameworks
- [ ] No magic numbers or strings
- [ ] No premature optimization
- [ ] No unnecessary abstractions

## Scalability & Performance

### Horizontal Scaling
- [ ] Stateless design where possible
- [ ] Session state externalized if needed
- [ ] No server affinity requirements
- [ ] Load balancer compatible

### Vertical Scaling
- [ ] Efficient resource usage
- [ ] Appropriate data structures
- [ ] No obvious performance bottlenecks
- [ ] Algorithms have reasonable complexity

### Caching Strategy
- [ ] Appropriate caching layers identified
- [ ] Cache invalidation strategy clear
- [ ] Cache key design is effective
- [ ] No cache stampede issues

### Database
- [ ] Proper indexing strategy
- [ ] No N+1 query problems
- [ ] Appropriate use of database features
- [ ] Connection pooling configured
- [ ] Query optimization considered

## Reliability & Resilience

### Error Handling
- [ ] Errors handled gracefully
- [ ] Appropriate error boundaries
- [ ] No silent failures
- [ ] Error messages are meaningful
- [ ] Errors logged properly

### Fault Tolerance
- [ ] Graceful degradation strategy
- [ ] Circuit breakers where appropriate
- [ ] Retry logic with backoff
- [ ] Timeouts configured
- [ ] Bulkheads/isolation where needed

### Data Consistency
- [ ] Transaction boundaries clear
- [ ] Consistency model appropriate (strong vs eventual)
- [ ] Race conditions addressed
- [ ] Optimistic/pessimistic locking where needed
- [ ] Idempotency considered for operations

## Security

### Authentication & Authorization
- [ ] Proper authentication mechanism
- [ ] Authorization at appropriate layers
- [ ] Principle of least privilege
- [ ] No security logic in presentation layer
- [ ] Role-based or policy-based access control

### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] Secure communication (TLS/SSL)
- [ ] No sensitive data in logs
- [ ] Input validation and sanitization
- [ ] Output encoding to prevent injection

### OWASP Top 10
- [ ] Injection attacks prevented (SQL, XSS, etc.)
- [ ] Broken authentication addressed
- [ ] Sensitive data exposure mitigated
- [ ] XML external entities (XXE) handled
- [ ] Broken access control prevented
- [ ] Security misconfiguration avoided
- [ ] Cross-site scripting (XSS) prevented
- [ ] Insecure deserialization handled
- [ ] Components are up-to-date
- [ ] Logging and monitoring in place

## Maintainability

### Code Quality
- [ ] Code is readable and self-documenting
- [ ] Consistent naming conventions
- [ ] Appropriate comments for complex logic
- [ ] No dead code
- [ ] No commented-out code blocks

### Testing
- [ ] Testable design (dependency injection)
- [ ] Unit tests for business logic
- [ ] Integration tests for components
- [ ] Test coverage is adequate
- [ ] Tests are maintainable

### Documentation
- [ ] Architecture documented (ADRs, diagrams)
- [ ] API contracts documented
- [ ] Complex algorithms explained
- [ ] Setup/deployment documented
- [ ] Known limitations documented

### Technical Debt
- [ ] Technical debt identified and tracked
- [ ] No quick fixes without plan to address properly
- [ ] Refactoring opportunities noted
- [ ] Dependencies are current

## Operational Concerns

### Observability
- [ ] Structured logging in place
- [ ] Appropriate log levels used
- [ ] Metrics/telemetry captured
- [ ] Distributed tracing if applicable
- [ ] Health check endpoints

### Configuration
- [ ] Configuration externalized
- [ ] Environment-specific config supported
- [ ] Secrets management proper
- [ ] Feature flags where appropriate
- [ ] Configuration validated on startup

### Deployment
- [ ] CI/CD friendly design
- [ ] Zero-downtime deployment possible
- [ ] Rollback strategy clear
- [ ] Database migrations handled
- [ ] Infrastructure as code

## Domain-Driven Design

### Domain Model
- [ ] Rich domain model (not anemic)
- [ ] Business logic in domain layer
- [ ] Entities vs Value Objects clear
- [ ] Aggregates properly defined
- [ ] Domain events where appropriate

### Bounded Contexts
- [ ] Clear context boundaries
- [ ] Context mapping documented
- [ ] No leaking abstractions
- [ ] Ubiquitous language used

## API Design

### RESTful APIs
- [ ] Proper HTTP verbs (GET, POST, PUT, DELETE)
- [ ] Appropriate status codes
- [ ] Resource-oriented design
- [ ] Versioning strategy
- [ ] Pagination for collections
- [ ] HATEOAS if applicable

### API Quality
- [ ] Consistent naming conventions
- [ ] Clear error responses
- [ ] API documentation (OpenAPI/Swagger)
- [ ] Rate limiting considered
- [ ] Backward compatibility maintained

## Cloud-Native Considerations

### 12-Factor App
- [ ] Codebase tracked in version control
- [ ] Dependencies explicitly declared
- [ ] Config stored in environment
- [ ] Backing services as attached resources
- [ ] Build, release, run stages separated
- [ ] Stateless processes
- [ ] Port binding for service export
- [ ] Concurrency via process model
- [ ] Fast startup and graceful shutdown
- [ ] Dev/prod parity
- [ ] Logs as event streams
- [ ] Admin tasks as one-off processes

## Review Questions to Ask

1. **Why was this approach chosen over alternatives?**
2. **What are the trade-offs of this design?**
3. **How will this scale as the system grows?**
4. **What happens if this component fails?**
5. **How easy is it to test this code?**
6. **Will this decision make future changes harder?**
7. **Is this solving a real problem or over-engineering?**
8. **How will we monitor this in production?**
9. **What are the security implications?**
10. **Does the team understand this approach?**

## Red Flags

Watch out for these warning signs:

- Tight coupling between layers
- Massive classes (>500 lines)
- Long methods (>50 lines)
- Deep nesting (>3-4 levels)
- Circular dependencies
- No tests or very low coverage
- Hard-coded configuration
- No error handling
- Copy-pasted code
- Unclear naming
- Mixed abstraction levels
- Framework lock-in
- No logging or monitoring
- Synchronous operations everywhere
- No caching strategy
- Missing documentation

## Positive Indicators

Look for these good practices:

- Clear separation of concerns
- Consistent patterns throughout
- Comprehensive test coverage
- Good naming conventions
- Appropriate abstractions
- Error handling strategy
- Monitoring and observability
- Documentation and ADRs
- Security by design
- Performance considerations
- Scalability planning
- Maintainable code structure
