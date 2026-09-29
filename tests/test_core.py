import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_feed(self):
        state = core.new_game()
        self.assertTrue(core.feed(state, 1, 10))
        self.assertFalse(core.feed(state, 1, 10))

    def test_02_reactor_capacity(self):
        state = core.new_game()
        state["reactor_load"] = 2
        result = core.react(state, 1)
        self.assertFalse(result)

    def test_03_temp_boundary(self):
        state = core.new_game()
        self.assertEqual(core.check_temp(state, 35), "over")

    def test_04_cancel_releases_reactor(self):
        state = core.new_game()
        core.react(state, 1)
        core.cancel(state, 1)
        self.assertEqual(state["reactor_load"], 0)

    def test_05_inspect_failure_refunds(self):
        state = core.new_game()
        core.feed(state, 1, 10)
        state["batches"][1]["defect"] = True
        before = state["material"]
        result = core.inspect(state, 1)
        self.assertFalse(result)
        self.assertEqual(state["material"], before + 10)

    def test_06_no_produce_on_fault(self):
        state = core.new_game()
        state["clean_fault"] = True
        result = core.produce(state, 5)
        self.assertFalse(result)

    def test_07_pollute_once(self):
        state = core.new_game()
        core.pollute(state)
        self.assertEqual(state["safety"], 90)

    def test_08_load_preserves_batch(self):
        state = core.new_game()
        state["batch_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["batch_id"], 4)


if __name__ == "__main__":
    unittest.main()
