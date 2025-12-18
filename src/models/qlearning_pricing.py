import numpy as np

class QLearningPricer:
    def __init__(self, base_price, elasticity=-1.2, learning_rate=0.1, discount=0.95, episodes=1000):
        self.base_price = base_price
        self.elasticity = elasticity
        self.lr = learning_rate
        self.gamma = discount
        
        # Q-table: 5 estados de demanda, 11 acciones de precio (-50% a +50%)
        self.q_table = np.zeros((5, 11))
    
    def get_state(self, demand_ratio):
        # Convertir ratio de demanda a estado 0-4
        return min(int(demand_ratio * 5), 4)
    
    def demand_function(self, price_ratio):
        # Función de demanda basada en elasticidad
        return max(price_ratio ** self.elasticity, 0.1)
    
    def train(self, episodes=500):
        base_demand = 1000
        for _ in range(episodes):
            state = np.random.randint(0, 5)
            action = np.random.randint(0, 11) if np.random.random() < 0.1 else np.argmax(self.q_table[state])
            
            price_change = (action - 5) * 0.1  # -0.5 a +0.5
            price_ratio = 1 + price_change
            demand = base_demand * self.demand_function(price_ratio)
            revenue = self.base_price * price_ratio * demand
            
            next_state = self.get_state(demand / base_demand)
            reward = revenue
            
            self.q_table[state, action] += self.lr * (reward + self.gamma * np.max(self.q_table[next_state]) - self.q_table[state, action])
    
    def get_optimal_price(self, current_demand_ratio=1.0):
        state = self.get_state(current_demand_ratio)
        action = np.argmax(self.q_table[state])
        price_change = (action - 5) * 0.1
        return self.base_price * (1 + price_change)