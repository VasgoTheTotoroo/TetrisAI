test = {
  'name': 'TetrisAI',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> board = Board([[0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
          ...                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
          ...                [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
          ...                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          ...                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]);
          >>> piece = Tetromino.create('T').move_to(1,2);
          >>> state = (board, piece);
          >>> 
          >>> policy = TetrisAI();
          >>> params = [0.17, 0.55, 0.16, 0.12];
          >>> action = policy(state, params);
          >>> 
          >>> action
          3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
