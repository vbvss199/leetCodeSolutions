class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # easy peasy 
        # consider the net gas = gas -cost 
        # initially net_gas=0 and start=0
        # and one more check if the total amount of gas is leasser then cost return -1 immediately 
        if(sum(gas)<sum(cost)):
            return -1

        net_gas=0
        start=0
        for i in range(0,len(cost)):
            # at any moment calculate the net_gas
            net_gas=net_gas+(gas[i]-cost[i])
            # if the net_gas at any point goes <0 then reset the net_gas and start from the next point 
            if(net_gas<0):
                net_gas,start=0,i+1
        return start