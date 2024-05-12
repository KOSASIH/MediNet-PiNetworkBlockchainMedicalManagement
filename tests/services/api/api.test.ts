import { ApiService } from './api';

describe('ApiService', () => {
  let apiService: ApiService;

  beforeEach(() => {
    apiService = new ApiService();
  });

  it('should fetch data from an API endpoint', async () => {
    const data = await apiService.fetchData('https://jsonplaceholder.typicode.com/todos/1');
    expect(data).toBeDefined();
    expect(data.id).toBe(1);
  });

  it('should handle API errors', async () => {
    const error = await apiService.fetchData('https://jsonplaceholder.typicode.com/invalid-endpoint');
    expect(error).toBeDefined();
    expect(error.message).toMatch(/Failed to fetch/);
  });
});
