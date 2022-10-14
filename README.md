# RoboAdvisor_4FD3
This is the capstone project of B.tech program in McMaster Univeristy, Fall 2022.
## Frond end
[ChatBot UI](./roboAdvisor/README.md)

## Backend
### MutualFund
```python
class mutualFund() {
  # should return the infomation of looking symbol
  def get(symbol) {}
  # should return the list of mutual funds that fall in the looking risk level
  def getRisk(level) {}
}

# How the frond end consumes the functions, e.g.
import mutualFund

mutualFund.get('RBF460.CF')
mutualFund.getRisk('Low')
```
