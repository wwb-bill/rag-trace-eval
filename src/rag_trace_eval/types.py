from dataclasses import dataclass

@dataclass
class ChunkStep:
    strategy: str; chunk_count: int; avg_chunk_size: int; duration_ms: float = 0
@dataclass
class RetrieveStep:
    query: str; retrieved_docs: int; top_k: int; duration_ms: float = 0
@dataclass
class GenerateStep:
    model: str; output: str; input_tokens: int; output_tokens: int; duration_ms: float = 0
@dataclass
class CiteStep:
    citations: list; covered: int; total: int; coverage: float; duration_ms: float = 0
@dataclass
class EvalTrace:
    id: str; document_id: str; chunk: ChunkStep|None = None; retrieval: RetrieveStep|None = None; generation: GenerateStep|None = None; citation: CiteStep|None = None; budget_tokens: int = 0; budget_used: int = 0