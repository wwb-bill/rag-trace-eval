# rag-trace-eval

Trace-linked RAG evaluation pipeline. **9th M project.** Chunking, retrieval, generation, citation with budget awareness.

```python
from rag_trace_eval import RAGTracer, generate_report
tracer = RAGTracer(budget_tokens=5000)
trace = tracer.start("doc-1")
tracer.record_chunk(trace, "sentence", 3, 150)
report = generate_report("eval", tracer.traces)
```

28 tests · 8 modules · v1.0.0 · MIT
