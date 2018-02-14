
from ..storage import SimKVStore


class SimKeyValueMemory(SimKVStore):
    def __init__(self, memory_id):
        super(SimKeyValueMemory, self).__init__()
        self.memory_id = memory_id

    @SimStatePlugin.memo
    def copy(self, memo): # pylint: disable=unused-argument
        return SimKeyValueMemory(memory_id=self.memory_id,
                                 store=self._store.copy())

from angr.sim_state import SimState
SimState.register_default('keyvalue_memory', SimKeyValueMemory)