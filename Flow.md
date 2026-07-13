# Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Run CLI]
    B --> C[Enter folder path]
    C --> D[Choose organization mode]
    D --> E{Mode?}
    E -->|Type| F[Organize by file type]
    E -->|Date| G[Organize by date]
    E -->|Keyword| H[Organize by keyword]
    F --> I[Move files]
    G --> I
    H --> I
    I --> J[Done]
```