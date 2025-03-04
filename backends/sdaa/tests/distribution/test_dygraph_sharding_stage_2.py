# BSD 3- Clause License Copyright (c) 2023, Tecorigin Co., Ltd. All rights
# reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY,OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)  ARISING IN ANY
# WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.

import unittest

from test_parallel_dygraph_mp_layers import TestMultipleCustomDevices


class TestDygraphShardingStage2(TestMultipleCustomDevices):
    backend = "sdaa"
    allocator_strategy = "auto_growth"
    devices = ["0", "1"]

    def test_dygraph_sharding_stage2(self):
        self.run_mnist_2_custom_devices(
            "sdaa_dygraph_group_sharded_stage2.py",
            self.backend,
            allocator_strategy=self.allocator_strategy,
            selected_gpus=self.devices,
        )

    def test_dygraph_sharding_stage2_offload(self):
        self.run_mnist_2_custom_devices(
            "sdaa_dygraph_group_sharded_stage2_offload.py",
            self.backend,
            allocator_strategy=self.allocator_strategy,
            selected_gpus=self.devices,
        )

    def test_dygraph_sharding_api(self):
        self.run_mnist_2_custom_devices(
            "sdaa_dygraph_group_sharded_api.py",
            self.backend,
            allocator_strategy=self.allocator_strategy,
            selected_gpus=self.devices,
        )

    def test_dygraph_sharding_stage2_loss_stable(self):
        self.run_mnist_2_custom_devices(
            "sdaa_dygraph_group_sharded_stage2_loss_stable.py",
            self.backend,
            allocator_strategy=self.allocator_strategy,
            selected_gpus=self.devices,
        )


if __name__ == "__main__":
    unittest.main()
