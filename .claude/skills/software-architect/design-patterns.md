# Design Patterns Reference

## Creational Patterns

### Singleton
- **Use when**: You need exactly one instance of a class
- **Caution**: Can introduce global state, difficult to test
- **Modern alternative**: Dependency injection with scoped lifetime

### Factory Method
- **Use when**: Object creation logic is complex or needs to be centralized
- **Benefits**: Decouples object creation from usage

### Builder
- **Use when**: Object construction requires many parameters or steps
- **Benefits**: Fluent API, immutable objects, clear construction process

### Prototype
- **Use when**: Creating objects by cloning is more efficient than new instances
- **Common in**: Object pools, configuration templates

## Structural Patterns

### Adapter
- **Use when**: Need to make incompatible interfaces work together
- **Common in**: Legacy system integration, third-party library wrapping

### Decorator
- **Use when**: Need to add behavior dynamically without inheritance
- **Benefits**: Follows Open/Closed principle, composition over inheritance

### Facade
- **Use when**: Need to simplify complex subsystem interfaces
- **Benefits**: Reduces coupling, provides clear API boundaries

### Proxy
- **Use when**: Need to control access, add lazy loading, or remote access
- **Types**: Virtual proxy, protection proxy, remote proxy

### Composite
- **Use when**: Working with tree structures or part-whole hierarchies
- **Common in**: UI components, file systems, organizational structures

## Behavioral Patterns

### Strategy
- **Use when**: Multiple algorithms can be swapped at runtime
- **Benefits**: Eliminates conditionals, follows Open/Closed principle

### Observer
- **Use when**: One-to-many dependency between objects
- **Common in**: Event systems, MVC, reactive programming

### Command
- **Use when**: Need to parameterize actions, queue operations, or support undo
- **Benefits**: Decouples sender from receiver, supports transactions

### Chain of Responsibility
- **Use when**: Multiple handlers can process a request
- **Common in**: Middleware pipelines, logging frameworks, validation chains

### Template Method
- **Use when**: Algorithm structure is fixed but steps vary
- **Benefits**: Code reuse through inheritance

### State
- **Use when**: Object behavior changes based on internal state
- **Benefits**: Eliminates complex conditionals, encapsulates state-specific behavior

## Modern Patterns

### Repository
- **Use when**: Abstracting data access layer
- **Benefits**: Testability, separation of concerns, database independence

### Unit of Work
- **Use when**: Managing database transactions across multiple repositories
- **Benefits**: Consistency, transaction management

### Dependency Injection
- **Use when**: Always (in modern applications)
- **Benefits**: Testability, flexibility, loose coupling

### Service Locator
- **Use when**: Legacy systems (prefer DI in new code)
- **Caution**: Can hide dependencies, makes testing harder

## Anti-Patterns to Avoid

### God Object
- Symptom: One class does too much
- Solution: Apply Single Responsibility Principle

### Spaghetti Code
- Symptom: No clear structure, high coupling
- Solution: Refactor to layers and modules

### Lava Flow
- Symptom: Dead code kept "just in case"
- Solution: Remove unused code, use version control

### Golden Hammer
- Symptom: Using same pattern for every problem
- Solution: Choose patterns based on actual needs

### Premature Optimization
- Symptom: Optimizing before measuring
- Solution: Profile first, optimize bottlenecks

## Pattern Selection Guidelines

1. **Start Simple**: Don't add patterns until you need them
2. **Follow YAGNI**: You Aren't Gonna Need It
3. **Measure Complexity**: Patterns should reduce, not increase complexity
4. **Consider Team**: Use patterns your team understands
5. **Document Decisions**: Explain why you chose specific patterns
