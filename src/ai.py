import copy

from src.player import Player

class AI(Player):
    def __init__(self, name, color, depth=2):
        super().__init__(name, color)
        self.depth = depth
        # احتمالات رمي العصي الأربعة (حسب قواعد كندال)
        self.probs = {1: 0.25, 2: 0.375, 3: 0.25, 4: 0.0625, 5: 0.0625}
        

    def play(self, game_state):
        # تنفيذ البحث عن أفضل حركة
        move = self.compute_best_move(game_state)
        return move # يعيد رقم المربع (Index)

    def evaluate(self, game_instance):
        
        # تابع التقييم (Heuristic) الذي يشرح "ذكاء" الـ AI
        score = 0
        # مكافأة للأحجار التي خرجت من اللوح (هدف الفوز)
        score += (7 - len(self.pieces)) * 100
        
        for cell in game_instance.board.grid:
            if cell.piece:
                mult = 1 if cell.piece.color == self.color else -1
                pos = cell.piece.pos
                score += pos * mult # كلما تقدم الحجر زادت قيمته
                
                # تقييم المربعات الخاصة (بيت الماء، بيت السعادة)
                if pos == 26: score -= 150 * mult # خطر بيت الماء
                if pos == 25: score += 50 * mult  # بيت السعادة
        return score

    def compute_best_move(self, game_state):
        game_instance = game_state["game_instance"]
        roll = game_state["roll"]
        moves = game_instance.get_available_moves(self, roll)
        
        if not moves: return None
        
        best_score = float('-inf')
        best_move = moves[0]
        
        for m in moves:
            temp_game = copy.deepcopy(game_instance)
            temp_game.move_piece(m, roll)
            # الانتقال لطبقة الخصم (Min)
            score = self.expectiminimax(temp_game, self.depth - 1, False)
            if score > best_score:
                best_score = score
                best_move = m
        return best_move

    def expectiminimax(self, game_instance, depth, is_maximizing):
        if depth == 0 or game_instance.is_game_over():
            return self.evaluate(game_instance)
        
        # هنا يتم استدعاء عقدة الحظ (Chance Node)
        return self.chance_node(game_instance, depth, is_maximizing)

    def chance_node(self, game_instance, depth, next_is_max):
        expected_val = 0
        for roll, prob in self.probs.items():
            # حساب القيمة المتوقعة بناءً على احتمالات الرمي
            # (التفاصيل البرمجية للاحتمالات)
            # ...
            pass 
        return expected_val