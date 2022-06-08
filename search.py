from persistence import DB
class Search:
    
    def _define_ope(self):
        if 'ope' in self._fields:
            value = self._args.pop('ope')
            return value.upper()
        return 'AND'

    def _create_query_principal(self):
        #Fields diferentes of date and order
        _conunter = 0
        query = 'SELECT * FROM FORECAST WHERE '
        self._ope = self._define_ope()
        complement_query = self._create_query_secondary()
        fields=list(self._args.keys())
        for field in fields:
            if field not in ['date_start', 'order']:
                _conunter+=1
                query+=f'{field.upper()}="{self._args.get(field)}"'
                if len(fields) != _conunter: 
                    query+=f' {self._ope} '
        return f'{query} {complement_query}'

    def _create_query_secondary(self):
        query = ''
        if 'date_start' in self._fields:
            query+= f' {self._ope} `DATE` BETWEEN "{self._args.get("date_start")}" AND DATE("now")'
            self._args.pop('date_start')
        if 'order' in self._fields:
            query+= f' ORDER BY ID {self._args.get("order")}'
            self._args.pop('order')
        else:
            query+= f'{self._ope} DATE("now")'
        return query

    def search_in_db(self,**kwargs):
        self._args = kwargs
        self._fields = list(kwargs.keys())
        self._ope = None 
        query = self._create_query_principal()
        response, fields = DB().get_information(query)
        values = []
        if len(response) > 0:
            for value in response:
                temp = {}
                for indx, v in enumerate(value):
                    temp.update({fields[indx]:v})
                values.append(temp)
            return values,query
        return values,query