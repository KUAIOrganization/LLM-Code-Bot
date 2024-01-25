inputTokensList = ['\t', '\n', ' ', '    ', '!', '"', '",', '":', '#', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '.",', '..', '...,', '/', '0', '1', '2', 
'3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '<=', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'Each', 'F', 'For', 'G', 'H', 'I', 'If', 'In', 'Input', 'It', 'J', 'K', 'L', 'M', 'N', 'NO', 'No', 'Note', 'O', 'Output', 'P', 'Print', 'Q', 'R', 'S', 'T', 'The', 'U', 'V', 'W', 'X', 'Y', 'YES', 'You', 'Z', '[', '\\', ']', '^', '_', 'a', 'a_', 'a_i', 'ab', 'able', 'ac', 'ack', 'ad', 'after', 'ag', 'ail', 'ain', 'ake', 'al', 'all', 'ally', 'am', 'an', 'and', 'ang', 'answer', 'ant', 'any', 'ap', 'ar', 'ard', 'are', 'array', 'as', 'ast', 'at', 'ate', 'ated', 'ation', 'av', 'b', 'be', 'bet', 'ble', 'bo', 'bu', 'but', 'by', 'c', 'can', 'car', 'case', 'cases', 'ce', 'cell', 'ces', 'ch', 'charact', 'choose', 'ck', 'co', 'colo', 'com', 'consist', 'contain', 'contains', 'cor', 'cri', 'd', 'day', 'de', 'dec', 'den', 'descri', 'di', 'differe', 'dig', 'ding', 'dist', 'do', 'does', 'ds', 'e', 'each', 'ect', 'ed', 'el', 'elements', 'em', 'en', 'end', 'ent', 'equal', 'er', 'ers', 'es', 'est', 'et', 'ex', 'exactly', 'example', 'examples', 'ext', 'f', 'fetched', 'fin', 'first', 'follow', 'following', 'for', 'form', 'fou', 'from', 'g', 'game', 'get', 'gh', 'given', 'go', 'gr', 'guaranteed', 
'h', 'has', 'have', 'he', 'her', 'his', 'ho', 'i', 'ic', 'ice', 'id', 'ide', 'ie', 'ies', 'if', 'ig', 'ight', 'il', 'ile', 'ill', 'im', 'in', 'inc', 'ing', 'input', 'int', 'integer', 'integers', 'ion', 'ip', 
'ir', 'is', 'ist', 'it', 'its', 'ity', 'ive', 'iz', 'j', 'k', 'ke', 'ks', 'l', 'ld', 'le', 'left', 'length', 'let', 'letters', 'line', 'lines', 'lit', 'll', 'lo', 'lower', 'lu', 'ly', 'm', 'ma', 'make', 'maximum', 'me', 'ment', 'min', 'minimum', 'mo', 'move', 'mult', 'n', 'n1', 'n2', 'n3', 'nam', 'nd', 'ne', 'need', 'next', 'ng', 'no', 'not', 'now', 'ns', 'nt', 'number', 'numbers', 'o', 'ob', 'of', 'ok', 'on', 'one', 'only', 'op', 'operation', 'or', 'order', 'ote', 'other', 'out', 'output', 'ow', 'p', 'pair', 'par', 'pe', 'per', 'pl', 'place', 'play', 'ple', 'po', 'point', 'position', 'positive', 'possible', 'presen', 'print', 'pro', 'problem', 'q', 'qu', 'r', 'range', 're', 'read', 'rect', 'red', 'res', 'resp', 'ri', 'right', 'ro', 'row', 'rs', 's', 'same', 'sample', 'se', 'second', 'sequence', 'sh', 'she', 'should', 'side', 'single', 'sk', 'so', 'some', 'sp', 'spac', 'spe', 'ss', 'st', 'status', 'str', 'string', 'sub', 'such', 'sum', 't', 'tal', 'te', 'ted', 'ter', 'test', 'th', 'than', 'that', 'the', 'them', 'then', 'there', 'they', 'third', 'this', 'three', 'tic', 'time', 'times', 'ting', 'tion', 'tions', 'to', 'tr', 'ts', 'tur', 'two', 'ty', 'u', 'ul', 'un', 'unt', 'up', 'ur', 'us', 'use', 'ust', 'ut', 'v', 'value', 've', 'ver', 'very', 'w', 'wants', 'way', 'we', 'wh', 'where', 'which', 'will', 'wise', 'with', 'wor', 'x', 'y', 'ya', 'you', 'z', '{', '|', '}', '~']

inputTokensList = ['\t', '\n', ' ', '    ', '!', '"', '#', '%', '&', "'", '(',')', '*', '+', '+=', ',', '-', 
'--', '.', '.",', '...','/', '//', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '<=', '=', '==', '>', '?', '?",', '@', 'A', 'After', 'Alice', 'All', 'An', 'As', 'At', 'B', 'Ber', 'Bob', 'C', 'D', 'E', 'Each', 'English', 'F', 'Find', 'For', 'G', 'H', 'He', 'Help', 'How', 'I', 'If', 'In', 'Input', 'It', 'J', 'K', 'L', 'Latin', 'Let', 'M', 'N', 'NO', 'No', 'Note', 'Now', 'O', 'On', 'One', 'Otherwise', 'Output', 'P', 'Petya', 'Polycarp', 'Print', 'Q', 'R', 'S', 'So', 'T', 'The', 'Then', 'There', 'This', 'Thus', 'To', 'U', 'V', 'Val', 'Vasya', 'W', 'We', 'X', 'Y', 'YES', 'Yes', 'You', 'Your', 'Z', '[', '\\', ']', '])', '],', '].', '^', '_', 'a', 'aa', 'ab', 'able', 'about', 'ac', 'ack', 'act', 'ad', 'add', 'ade', 'after', 'ag', 'age', 'ain', 'air', 'ak', 'al', 'all', 'allow', 'ally', 'already', 'also', 'always', 'am', 'amount', 'an', 'ance', 'and', 'angle', 'another', 'ans', 'answer', 'answers', 'ant', 'any', 'ap', 'appe', 'ar', 'ard', 'are', 'arr', 'arrange', 'array', 'ars', 'ary', 'as', 'ase', 'asha', 'ass', 'ast', 'at', 'ate', 'ated', 'ately', 'ates', 'ating', 'ation', 'ations', 'ator', 'aut', 'av', 'available', 'ave', 'aw', 'ay', 'b',
 'ball', 'bb', 'be', 'because', 'becomes', 'before', 'beg', 'between', 'bit', 'black', 'blo', 'board', 'book', 'bot', 'both', 'box', 'br', 'break', 'buil', 'but', 'buy', 'by', 'c', 'calcul', 'call', 'can', 'candies', 'cannot', 'car', 'card', 'cards', 'case', 'cases', 'ce', 'cell', 'cells', 'cent', 'ces', 'cess', 'ch', 'change', 'character', 'characters', 'child', 'cho', 'choose', 'city', 'ck', 'cks', 'cl', 
'co', 'color', 'colum', 'com', 'con', 'conside', 'consisting', 'consists', 'contain', 'contains', 'coordin', 'correct', 'correspond', 'count', 'cr', 'ct', 'current', 'cut', 'd', 'day', 'days', 'de', 'dec', 'decided', 'decre', 'def', 'denot', 'der', 'describ', 'described', 'description', 'determine', 'di', 'differ', 'different', 'digit', 'digits', 'ding', 'direct', 'dis', 'distance', 'distinct', 'divisible', 'do', 'does', 'doesn', 'don', 'dots', 'down', 'dr', 'ds', 'during', 'dy', 'e', 'each', 'ect', 'ed', 'edge', 'ee', 'either', 'el', 'element', 'elements', 'else', 'em', 'empty', 'en', 'ence', 'end', 'ent', 'ep', 'equal', 'equals', 'er', 'ers', 'es', 'ess', 'est', 'et', 'eter', 'ets', 'ev', 'even', 'ever', 'every', 'ew', 'ex', 'exactly', 'example', 'examples', 'exceed', 'exists', 'ext', 'ey', 'f', 'fetched', 'ff', 'fin', 'find', 'first', 'fl', 'floor', 'follow', 'following', 'follows', 'for', 'form', 'four', 'fourth', 'friend', 'friends', 'from', 'ful', 'g', 'game', 'ge', 'get', 'give', 'given', 'go', 'good', 'gor', 'got', 'gr', 'graph', 'gre', 'greater', 'group', 'gu', 'guaranteed', 'h', 'ha', 'has', 'hat', 'have', 'he', 'height', 'help', 'her', 'him', 'his', 'ho', 'hold', 'house', 'how', 'i', 'ia', 'ial', 'ib', 'ic', 'ical', 'ically', 'ice', 'ices', 'ick', 'id', 'ie', 'ied', 'ies', 'if', 'ig', 'igh', 'ight', 'ign', 'ik', 'il', 'ile', 'ill', 'im', 'imal', 'impossible', 'in', 'ince', 'incl', 'increas', 'index', 'indi', 'ine', 'ing', 'initial', 'inn', 'input', 'int', 'integer', 'integers', 'inter', 'into', 'ion', 'ions', 'ip', 'ir', 'is', 'ise', 'ist', 'isting', 'it', 'ite', 'ith', 'its', 'ity', 'ive', 'ix', 'iz', 'j', 'k', 'ka', 'ked', 
'king', 'know', 'ks', 'l', 'lace', 'lan', 'land', 'large', 'last', 'ld', 'le', 'least', 'left', 'len', 'length', 'les', 'less', 'let', 'letter', 'letters', 'level', 'lex', 'like', 'line', 'lines', 'list', 'll', 'lo', 'loc', 'long', 'look', 'low', 'lower', 'lowercase', 'lue', 'ly', 'm', 'make', 'man', 'many', 'map', 'mar', 'mat', 'match', 'math', 'max', 'maximum', 'may', 'me', 'means', 'membe', 'ment', 'mer', 'min', 'minimum', 'minutes', 'mo', 'moment', 'mon', 'more', 'most', 'move', 'moves', 'ms', 'multiple', 'must', 'n', 'n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'nNO', 'nYES', 'name', 'nd', 'nds', 'ne', 'need', 'needs', 'negative', 'ner', 'new', 'next', 'ng', 'no', 'non', 'not', 'notes', 'now', 'ns', 'nt', 'num', 'number', 'numbered', 'numbers', 'o', 'obtain', 'occ', 'od', 'ode', 'of', 'off', 'oin', 'ol', 'on', 'once', 
'one', 'ones', 'ong', 'only', 'op', 'open', 'operation', 'operations', 'optimal', 'or', 'order', 'ore', 'ors', 'ose', 'ost', 'ote', 'other', 'otherwise', 'ough', 'ound', 'our', 'ous', 'out', 'output', 'ove', 
'over', 'ow', 'ower', 'oy', 'p', 'pair', 'pairs', 'palindrom', 'par', 'part', 'participant', 'pass', 'path', 'pe', 'people', 'per', 'perform', 'permutation', 'person', 'picture', 'pie', 'pl', 'place', 'plan', 'play', 'player', 'players', 'ple', 'po', 'point', 'points', 'port', 'position', 'positions', 'positive', 'possible', 'pre', 'press', 'pri', 'print', 'pro', 'problem', 'program', 'put', 'q', 'qu', 'query', 'quest', 'quotes', 'r', 'range', 're', 'reach', 'read', 'receive', 'red', 'remain', 'remove', 'replace', 'represen', 'required', 'respectively', 'result', 'return', 'rid', 'right', 'rightarrow', 'ro', 'room', 'round', 'row', 'rows', 'rs', 'ry', 's', 's_', 'same', 'sample', 'satisf', 'score', 'se', 'second', 'seconds', 'section', 'segment', 'select', 'self', 'sent', 'separated', 'sequence', 'ser', 'set', 'several', 'sh', 'she', 'should', 'show', 'shown', 'sid', 'sim', 'sing', 'single', 'size', 'sk', 'small', 'smallest', 'so', 'solution', 'solve', 'some', 'sor', 'space', 'spe', 'spec', 'split', 'square', 'ss', 'st', 'stand', 'star', 'state', 'status', 'step', 'stick', 'str', 'strict', 'string', 'strings', 'student', 'students', 'su', 'sub', 'subsequence', 'substring', 'such', 'sum', 'sw', 'sy', 't', 'table', 'take', 'task', 'te', 'team', 'ted', 'ter', 'test', 'tex', 'th', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'third', 'this', 'three', 'tic', 'time', 'times', 'ting', 'tion', 'tions', 'tle', 'to', 'ton', 'too', 'top', 'total', 'tr', 'train', 'tri', 'ts', 'tt', 'turn', 'two', 'ty', 'type', 'u', 'ub', 'uck', 'uct', 'ue', 'ugh', 'uld', 'ult', 'um', 'un', 'under', 'up', 'upper', 'ur', 'ure', 'urs', 'us', 'use', 'using', 'ut', 'ute', 'v', 'valid', 'value', 'values', 've', 'ver', 'vert', 'very', 'ves', 'vi', 'vide', 'ving', 'vis', 'w', 'want', 'wants', 'was', 'water', 'way', 'ways', 'we', 'weigh', 'wer', 'were', 'wh', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'will', 'win', 'with', 'without', 'won', 'wor', 'word', 'words', 'would', 'write', 'written', 'x', 'y', 'year', 'you', 'your', 'z', 'zero', '{', '|', '}', '~']

inputTokensList = ['\t', '\n', ' ', '    ', '!', '"', '#', '%', '&', "'", '(', ')', '*', '+', '++', '+=', ',', '-', '--', '.', '/', '//', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '<=', '=', '==', '>', '>=', '?', '@', 'A', 'After', 'Alice', 'All', 'Also', 'An', 'Ar', 'As', 'At', 'B', 'BB', 'Berland', 'Bob', 'But', 'C', 'Ch', 'Code', 'Consider', 'D', 'Determine', 'E', 'Each', 'English', 'Every', 'F', 'Find', 'First', 'For', 'G', 'Given', 'H', 'He', 'Help', 'However', 'I', 'If', 'In', 'Initially', 'Input', 'It', 'J', 'K', 'L', 'Latin', 'Let', 'Limak', 'M', 'ME', 'N', 'NO', 'Next', 'No', 'Note', 'Now', 'O', 'On', 'One', 'Otherwise', 'Output', 'P', 'Petya', 'Please', 'Pol', 'Polycarpus', 'Print', 'Q', 'R', 'RR', 'Re', 'S', 'Ser', 'She', 'Since', 'So', 'T', 'That', 'The', 'Then', 'There', 'They', 'This', 'Thus', 'To', 'Two', 'U', 'Un', 'V', 'Valera', 'Vasya', 'W', 'WW', 'We', 'What', 'When', 'X', 'Y', 'YES', 'Yes', 'You', 'Your', 'Z', '[', '\\', '\\"', '\\\\', ']', '^', '_', '_1', '_2', '_i', 'a', 'a_', 'a_1', 'a_2', 'a_3', 'a_i', 'a_n', 'aa', 'ab', 'aba', 'abc', 'able', 'about', 'above', 'absolute', 'ac', 'ach', 'ack', 'act', 'action', 'ad', 'add', 'adjacent', 'after', 'ag', 'again', 'age', 'ail', 'ain', 'air', 'ake', 'al', 'algorithm', 'all', 'allowed', 'ally', 'already', 'als', 'also', 'alt', 'always', 'am', 'among', 'amount', 'an', 'ance', 'and', 'ane', 'ang', 'ank', 'another', 'answer', 'answers', 'ant', 'any', 'ap', 'appe', 'appears', 'apple', 'ar', 'arbitrary', 'ard', 'are', 'area', 'arr', 'arrange', 'array', 'arrays', 'ars', 'art', 'ary', 'as', 
'ase', 'ash', 'asha', 'asked', 'assign', 'assume', 'ast', 'at', 'ate', 'ated', 'ately', 'ates', 'ating', 'ation', 'ations', 'ator', 'att', 'au', 'av', 'available', 'avel', 'ax', 'ay', 'az', 'b', 'b_', 'b_1', 
'b_2', 'b_i', 'bag', 'ball', 'bar', 'bb', 'bc', 'be', 'beautiful', 'because', 'become', 'becomes', 'been', 'before', 'beginning', 'belong', 'ber', 'between', 'binary', 'bit', 'black', 'ble', 'block', 'blue', 
'bo', 'board', 'book', 'bot', 'both', 'box', 'br', 'brack', 'break', 'bstring', 'build', 'bur', 'bus', 'but', 'button', 'buy', 'by', 'c', 'c_', 'cal', 'calculate', 'call', 'called', 'came', 'can', 'candies', 
'cannot', 'cap', 'car', 'card', 'cards', 'carp', 'case', 'cases', 'cd', 'ceil', 'cell', 'cells', 'cent', 'cep', 'ces', 'ch', 'change', 'character', 'characters', 'check', 'chess', 'child', 'cho', 'choose', 'chooses', 'chosen', 'cide', 'cities', 'city', 'ck', 'cks', 'cl', 'class', 'cle', 'clo', 'clu', 'code', 'coin', 'coins', 'col', 'coll', 'color', 'colors', 'column', 'columns', 'com', 'come', 'common', 'comp', 'complet', 'con', 'condition', 'conditions', 'connec', 'consecutive', 'consider', 'considered', 'consist', 'consisting', 'consists', 'constr', 'cont', 'contain', 'containing', 'contains', 'contest', 'coordinate', 'coordinates', 'cor', 'cording', 'correct', 'correspon', 'corresponding', 'cost', 'could', 'count', 'cr', 'cre', 'cup', 'current', 'cus', 'cut', 'cy', 'd', 'data', 'day', 'days', 'dd', 'de', 'decided', 'decimal', 'decreas', 'def', 'delet', 'denote', 'denotes', 'denoting', 'depen', 'der', 'des', 'describ', 'described', 'description', 'determine', 'dev', 'dia', 'did', 'diff', 'difference', 'different', 'digit', 'digits', 'ding', 'direction', 'dis', 'distance', 'distinct', 'distr', 'divide', 'divis', 'divisible', 'do', 'does', 'doesn', 'doll', 'domin', 'don', 'door', 'dots', 'down', 'dr', 'draw', 'ds', 'during', 'dy', 'e', 'each', 'ead', 'ear', 'eas', 'eat', 'ect', 'ecutive', 'ed', 'edge', 'ee', 'eep', 'eg', 'either', 'el', 'element', 'elements', 'elevator', 'ell', 'else', 'ely', 'em', 'empty', 'en', 'ence', 'end', 'ends', 'enough', 'ens', 'ent', 'ep', 'equ', 'equal', 'equals', 'er', 'ers', 'es', 'ess', 'est', 'et', 'ets', 'ev', 'even', 'ever', 'every', 'ew', 'ex', 'exactly', 'example', 'examples', 'exceed', 'exist', 'exists', 'ey', 'f', 'fav', 'fetched', 'ff', 'field', 'fifth', 'fig', 'fil', 'fill', 'final', 'find', 'finish', 'finite', 'first', 'fl', 'floor', 'follow', 'following', 'follows', 'for', 'forces', 'fore', 'form', 'found', 'four', 'fourth', 'fr', 'friend', 'friends', 'from', 'ful', 'fun', 'g', 'game', 'ge', 'gener', 'ger', 'get', 'gets', 'gir', 'give', 'given', 'go', 'goal', 'goes', 'going', 'good', 'got', 'gra', 'graph', 'gre', 'greater', 'grid', 'group', 'groups', 'gu', 'guaranteed', 'gular', 'gy', 'h', 'ha', 'had', 'hand', 'happ', 'has', 'have', 'he', 'height', 'help', 'her', 'hig', 'him', 'his', 'hold', 'home', 'hor', 'hour', 
'house', 'how', 'ht', 'hy', 'i', 'ia', 'ial', 'ian', 'ibut', 'ic', 'ical', 'ice', 'ick', 'id', 'ide', 'ie', 'ied', 'ient', 'ier', 'ies', 'if', 'ific', 'ift', 'ig', 'ight', 'ik', 'il', 'ill', 'ily', 'im', 'imize', 'impossible', 'in', 'inclusive', 'increas', 'increasing', 'ind', 'index', 'indices', 'ine', 'ined', 'information', 'ing', 'initial', 'initially', 'ink', 'input', 'inst', 'integer', 'integers', 'inter', 'interest', 'intersect', 'into', 'io', 'ion', 'ions', 'ip', 'ir', 'irect', 'is', 'it', 'ite', 'items', 'ition', 'its', 'ittle', 'ity', 'iv', 'ive', 'ivers', 'ives', 'ix', 'iz', 'ized', 'j', 'ject', 'jump', 'just', 'k', 'ka', 'key', 'king', 'know', 'known', 'knows', 'ks', 'l', 'lace', 'land', 'language', 'large', 'last', 'late', 'ld', 'le', 'leading', 'least', 'leave', 'lect', 'left', 'length', 'lengths', 'les', 'less', 'let', 'letter', 'letters', 'level', 'lex', 'lexicographically', 'lf', 'light', 'like', 'likes', 'lim', 'line', 'lines', 'list', 'll', 'lly', 'lo', 'located', 'log', 'long', 'look', 'low', 'lower', 'lowercase', 'ls', 'lt', 'lucky', 'lus', 'ly', 'm', 'm_input', 'ma', 'made', 'mag', 'make', 'man', 'many', 'map', 'mark', 'mat', 'match', 'math', 'matrix', 'max', 'maximum', 'may', 'me', 'means', 'mediate', 'meet', 'member', 'members', 'ment', 'ments', 'mer', 'message', 'met', 'min', 'minimal', 'minimum', 'minute', 'minutes', 'mo', 'mod', 'moment', 'money', 'monster', 'more', 'most', 'move', 'moves', 'ms', 'much', 'multiple', 'must', 'n', 'n0', 'n1', 'n10', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'nNO', 'nYES', 'na', 'name', 'names', 'nce', 'nd', 'nds', 'ne', 'necess', 'ned', 'need', 'needed', 'needs', 'negative', 'neighb', 
'ner', 'new', 'next', 'ng', 'night', 'ning', 'nnec', 'no', 'non', 'not', 'note', 'notes', 'now', 'ns', 'nt', 'nts', 'num', 'number', 'numbered', 'numbers', 'o', 'ob', 'obtain', 'obtained', 'oc', 'occur', 'ock', 'odd', 'oes', 'of', 'off', 'ok', 'ol', 'om', 'on', 'once', 'one', 'ones', 'ong', 'only', 'ons', 'ont', 'oo', 'op', 'open', 'operation', 'operations', 'operator', 'optimal', 'or', 'order', 'ore', 'ors', 'os', 'ose', 'oss', 'ot', 'ote', 'otes', 'other', 'otherwise', 'ough', 'our', 'ous', 'out', 'output', 'over', 'ow', 'ower', 'oy', 'p', 'p_', 'p_i', 'pack', 'page', 'paint', 'pair', 'pairs', 'palindrome', 'paper', 'par', 'part', 'partic', 'participant', 'participants', 'parts', 'pass', 'path', 'pay', 'pe', 'people', 'per', 'perform', 'permutation', 'person', 'ph', 'picture', 'piece', 'pieces', 'pile', 'pl', 'place', 'plan', 'play', 'player', 'players', 'playing', 'ple', 'ply', 'point', 'points', 'pol', 'port', 'pos', 'position', 'positions', 'positive', 'possible', 'possibly', 'post', 'power', 'pr', 'pre', 'pref', 'present', 'press', 'price', 'prime', 'print', 'pro', 'problem', 'problems', 'process', 'prod', 'program', 'put', 'q', 'qu', 'que', 'queries', 'query', 'question', 'quotes', 'r', 'range', 'rating', 'rd', 're', 'reach', 'read', 'receive', 'reco', 'rectangle', 'red', 'remain', 'remaining', 'remove', 'ren', 'replace', 'represent', 'represented', 'representing', 'required', 'respectively', 'rest', 'result', 'resulting', 'return', 'ric', 'rid', 'right', 'rightarrow', 'ris', 'ro', 'road', 'robot', 'roo', 'room', 'round', 'row', 'rows', 'rs', 'rt', 'rul', 'run', 'ry', 's', 's_', 'sa', 'same', 'sample', 'satisf', 'satisfy', 'school', 'score', 'se', 'seat', 'second', 'seconds', 'section', 'sed', 'see', 'segment', 'segments', 'select', 'self', 'sent', 'separated', 'sequence', 'sequences', 'ser', 'ses', 'set', 'sets', 'several', 'sh', 'she', 'shop', 'should', 'show', 'shown', 'shows', 'side', 'sides', 'sig', 'sim', 'since', 'sing', 'single', 'sit', 'size', 'sk', 'skill', 'sl', 'small', 'smallest', 'so', 'soldier', 'solution', 'solutions', 'solve', 'some', 'sorted', 'sp', 'space', 'spaces', 'spec', 'spell', 'spend', 'split', 'square', 'squares', 'ss', 'st', 'stand', 'standing', 
'start', 'starting', 'starts', 'statement', 'station', 'status', 'step', 'steps', 'stick', 'sticks', 'still', 'stones', 'stop', 'store', 'stra', 'stre', 'strictly', 'string', 'strings', 'student', 'students', 'sub', 'subsequence', 'substring', 'success', 'such', 'suit', 'sum', 'sup', 'sur', 'swap', 'system', 't', 'table', 'take', 'takes', 'tan', 'task', 'tate', 'te', 'team', 'teams', 'ted', 'ter', 'ters', 'tes', 
'test', 'testcase', 'text', 'texttt', 'th', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thing', 'third', 'this', 'three', 'through', 'tic', 'tile', 'time', 'times', 'ting', 'tion', 'tions', 'to', 'too', 'top', 'tor', 'total', 'town', 'tr', 'train', 'trans', 'tree', 'triangle', 'ts', 'tunately', 'turn', 'turns', 'tw', 'two', 'ty', 'type', 'types', 'u', 'ub', 'uc', 'uct', 'ue', 'uff', 'ug', 'ul', 'ular', 'ult', 'um', 'ume', 'un', 'under', 'unt', 'up', 'upper', 'uppercase', 'ur', 'ure', 'urs', 'us', 'use', 'used', 'using', 'ut', 'ute', 'v', 'valid', 'value', 'values', 've', 'ved', 'ven', 'ver', 'vertices', 'very', 'ves', 'vice', 'vie', 'ving', 'vious', 'visit', 'w', 'walk', 'want', 'wants', 'ward', 'was', 'watch', 'water', 'way', 'ways', 'we', 'weight', 'well', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'white', 'who', 'whole', 'will', 'win', 'winner', 'wins', 'wise', 'with', 'without', 'won', 'word', 'words', 'work', 'would', 'wr', 'write', 'written', 'x', 'x_1', 'x_i', 'y', 'ya', 'year', 'ym', 'you', 'your', 'ys', 'z', 'zero', 'zz', '{', '|', '}', '~']

outputTokensList = ['\t', '\n', ' ', '!', '!=', '"', '#', '%', '&', "'", '(', ')', '*', '+', '++', ',', '-', '--', '.', '/', '//', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '<=', '=', '==', '>', '>=', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'False', 'Friendship', 'G', 'H', 'HA', 'I', 'IO', 'J', 'K', 'L', 'M', 'N', 'NO', 'O', 'P', 'Q', 'R', 'S', 'St', 'T', 'True', 'U', 'V', 'W', 'X', 'Y', 'YES', 'Z', '[', 
'\\', ']', '^', '_', '__', '__main__', '__name__', 'a', 'a1', 'a3', 'ab', 'abs', 'act', 'actual', 'ad', 'al', 'an', 'and', 'ans', 'ans1', 'ap', 'append', 'ar', 'ard', 'arr', 'array', 'at', 'b', 'bi', 'bo', 'break', 'buffer', 'bur', 'c', 'c1', 'c2', 'ca', 'case', 'ce', 'ces', 'ch', 'char', 'ck', 'cnt', 'co', 'con', 'continue', 'cor', 'count', 'counter', 'ct', 'current_', 'd', 'data', 'de', 'def', 'di', 'diff', 'dist', 'distance', 'dp', 'dragon', 'e', 'ed', 'elif', 'else', 'em', 'ence', 'end', 'ent', 'ep', 'er', 'es', 'et', 'ew', 'ex', 'f', 'fi', 'fl', 'flag', 'for', 'fro', 'g', 'ges', 'get', 'h', 'hate', 'he', 'hedron', 'hl', 'i', 'ial', 'if', 'ig', 'im', 'import', 'in', 'ind', 'index', 'ing', 'input', 'int', 'ion', 'ions', 'is', 'ishka', 'it', 'j', 'join', 'k', 'key', 'l', 'la', 'lambda', 'le', 'lef', 'len', 'les', 'letter', 'line', 'list', 'll', 'love', 'lower', 'ls', 'lst', 'm', 'ma', 'main', 'map', 'math', 'max', 'max_', 'maxi', 'mi', 'min', 'min_', 'mo', 'mp', 'my', 'mylist', 'n', 'name', 'nd', 'new', 'nl', 'no', 'not', 'np', 'nt', 'num', 'num_', 'num_candles', 'number', 'numbers', 'nums', 'o', 'odd', 'of', 'ol', 
'on', 'one', 'open', 'or', 'os', 'ou', 'out', 'output', 'ow', 'p', 'pa', 'pas', 'per', 'pla', 'planes', 'point', 'pos', 'pre', 'price', 'print', 'problem', 'q', 'r', 'r1', 'r2', 'range', 'raw', 're', 'read', 
'readline', 'remov', 'res', 'result', 'return', 'ri', 'right', 'rin', 'ris', 'rs', 'rst', 's', 's1', 's2', 's_', 'score', 'scores', 'se', 'self', 'set', 'sh', 'si', 'solve', 'sort', 'sorted', 'split', 'ssi', 
'st', 'stdin', 'stdout', 'steps', 'str', 'str1', 'str_1', 'string', 'strip', 'sub', 'sum', 'sys', 't', 't1', 't_', 'te', 'tes', 'th', 'that', 'the', 'time', 'to', 'toasts', 'total', 'ts', 'u', 'ue', 'um', 'up', 'ut', 'v', 'val', 've', 'vi', 'vowel', 'w', 'while', 'word', 'write', 'x', 'x1', 'x2', 'y', 'z', '{', '|', '}', '~']

import re
import json
import glob
import os
from common.Tokenization.Tokenizer import Tokenizer
import tokenize

#Output file locations:
TOKEN_FOLDER_LOCATION = "C:\\AIClub\\Code\\Large Dataset\\Tokenized2" #The folder to output into
TOKEN_FILE_LOCATION = TOKEN_FOLDER_LOCATION + "\\tokens.json"#The file to put the tokens into (just a list of the tokens)
TOKENIZED_PROBLEMS_LOCATION = TOKEN_FOLDER_LOCATION + "\\problem_tokenized_" # The names of the files for each of the tokenized problems (each one will have the problem number tacked on the end)
TOKENIZED_SUBMISSIONS_LOCATION = TOKEN_FOLDER_LOCATION + "\\submission_tokenized_" # The names of the files for each of the tokenized solutions (same as above)

class Load:
    def __init__(self, problems_path, submissions_dir):
        self.problems_path = problems_path
        self.submissions_dir = submissions_dir
        self.problems = {}
        self.solutions = []
        self.tokenizer: Tokenizer = Tokenizer((inputTokensList, [i+1 for i in range(len(inputTokensList))]))
        self.outTokenizer: Tokenizer = None#None if outputTokensList is None else Tokenizer((outputTokensList, [i+1 for i in range(len(outputTokensList))]))
        self.problem_padded = None
        self.solution_padded = None
        self.dataset = None
        self.seqLen = 0
        self.seqLenSol = 0

    def load_problems(self):
        # Load problem descriptions
        with open(self.problems_path, 'r') as f:
            problems_list = json.load(f)

        # Populate self.problems as a dictionary
        for problem in problems_list:
            id = problem.get('problem_id', '') # Unused
            statement = problem.get('problem_statement', '')
            input = problem.get('problem_input', '')
            output = problem.get('problem_output', '')
            notes = problem.get('problem_notes', '')
            examples = problem.get('examples', '')

            # Concatenate attributes using hyperidentifiers
            concatenated_problem = f"XXSTATEMENT {statement} XXINPUT {input} XXOUTPUT {output} XXNOTES {notes} XXEXAMPLES {examples}"
            self.problems[id] = concatenated_problem

    def load_solutions(self):
        solution_sequences = []
        # Load code solutions into self.solutions list
        max = 0
        index  = 0
        maxIndex = 0
        for filepath in glob.glob(f"{self.submissions_dir}/*.py"):
            filename = os.path.basename(filepath)
            #print("filename: ", filename)

            # Extract the problem number of the submission
            problem_number = int(re.findall(r'^\d+', filename)[0])
            # Extract the matching problem
            problem_content = self.problems.get(int(problem_number), None)
            if problem_content is None:
                print("This problem has no content:", problem_number)

            with open(filepath, "r") as f:
                sol = []
                for token in tokenize.generate_tokens(f.readline):
                    sol += self.tokenize(token.exact_type, token.string)
                solution_sequences.append(sol)
                if(max < len(sol)):
                    max = len(sol)
                    maxIndex = index
                    #print(problem_number)
            with open(filepath, "r") as f:
                self.solutions.append((problem_number, f.read()))
            index += 1
            
        for sol in solution_sequences:
            for i in range(max - len(sol)):
                sol.append(["", ""])#sol.append([-1, -1])
        self.solution_padded = solution_sequences
        self.seqLenSol = max
        #print("Max:", str(max))
        #print("Index:", str(maxIndex))

    def tokenize(self, type: int, string: str) -> list[list[int | str]]:
        if self.outTokenizer is None:
            return [[type, string]]
        
        tokenized = self.outTokenizer.tokenize(string)
        return [[token, type] for token in tokenized]

    def tokenize_and_pad(self):
        # Searches for matching problems for each solution
        max = 0
        problem_sequences = []
        #solution_sequences = []
        for problem_number, solution in self.solutions:
            #print(problem_number)
            problem_content = self.problems.get(problem_number)
            problem_sequence = self.tokenizer.tokenize(problem_content)
            if len(problem_sequence) > max:
                max = len(problem_sequence)
                #print(problem_number, max)
            problem_sequences.append(problem_content)#problem_sequences.append(problem_sequence)
        #print("Max: " + str(max))
        self.seqLen = max

        self.problem_padded = problem_sequences#[pad(sequence, max, -1) for sequence in problem_sequences]

    def store(self):
        for i in range(len(self.problem_padded)):
            pFile = open(TOKENIZED_PROBLEMS_LOCATION + str(i) + ".txt", "w")
            sFile = open(TOKENIZED_SUBMISSIONS_LOCATION + str(i) + ".txt", "w")
            pFile.write(str(self.problem_padded[i]))
            #for j in range(self.seqLen):
            #    pFile.write(str(self.problem_padded[i][j]) + " ")
            for j in range(self.seqLenSol):
                sFile.write(str(self.solution_padded[i][j][1]) + " ")
                #sFile.write((str(self.solution_padded[i][j][0]) + " " + str(self.solution_padded[i][j][1]) + "|") if self.outTokenizer is None else (str(self.solution_padded[i][j][0]) + " " + str(self.solution_padded[i][j][1]) + " "))

            pFile.flush()
            sFile.flush()
            pFile.close()
            sFile.close()

        tokenFile = open(TOKEN_FILE_LOCATION, "w")
        for token in inputTokensList:
            tokenFile.write(token + " ")
        tokenFile.flush()
        tokenFile.close()

def pad(sequence: list[int], length: int, padToken: int):
    return sequence + [padToken for i in range(length - len(sequence))]

def main():
    load = Load("C:\\AIClub\\Code\\Large Dataset\\A_Problems_Clean.json", "C:\\AIClub\\Code\\Large Dataset\\A_Submissions_Cleaned")
    load.load_problems()
    load.load_solutions()
    load.tokenize_and_pad()
    load.store()

if __name__ == "__main__":
    main()