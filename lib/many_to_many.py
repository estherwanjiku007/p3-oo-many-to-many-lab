class Author:
    def __init__(self,name):      
        self.name=name
        self._contracts=[]
    
    def books(self):
    #   all_author_books=[]
    #   my_books= [all_books for all_books in Contract.my_contracts  if Contract.author==self.name]
    #   for a in range(len(my_books)) :
    #       all_author_books.append(my_books[a]["book"])
     # return [all_contracts.book for all_contracts in Contract.my_contracts if Contract.author==self]
       return list(set(all_contracts.books for all_contracts in self._contracts if isinstance(all_contracts.author,Contract.author)))
   
    # def contracts(self):
    #    # return [all_contracts for all_contracts in self._contracts  ]
    #      return self._contracts# list(set(all_contracts for all_contracts in self._contracts ))

    def sign_contract(self,book,date,royalties):
        contract=Contract(self,book,date,royalties)
        self._contracts.append(contract)
     
    def contracts(self):
        #return [all_contracts for all_contracts in Contract.my_contracts  if Contract.author==self.name]
         return [contracts for contracts in self._contracts ]

    def total_royalties(self):
        all_royalties=0
        for contracts in Contract.my_contracts :
          if Contract.author==self:
           all_royalties+=contracts.royalties
        

class Book:
    my_books=[]
    def __init__(self,title):
       # self.name=name
        self.title=title
        self.my_books.append(self)

    def books(self):
        return self.my_books 

    def authors(self):
        for author in Author.contracts:
         if isinstance(self.title,author.title):
           return author.name 
    def contracts(self):
        for contract in Contract.my_contracts:
            return contract

class Contract:
    my_contracts=[]
    def __init__(self,author,book,date,royalties):
        if isinstance(author,Author):
            self.author=author
        else:raise Exception("Author must be an instance of author")
       
        if isinstance(book,Book):
            self._book=book
        else:raise Exception("Book must be an instance of book class")
        #self._book=book
        if isinstance(date,str):
            self.date=date
        else:raise Exception("Date must be  string")
        if isinstance(royalties,int):
            self.royalties=royalties
        else:raise Exception("Royalties must be a string")
        self.my_contracts.append(self)    
        #Contract.contract_by_date(date)
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):     

               if isinstance(author,Author):
                self._author=author
        
               else:raise Exception("Author must be an instance of author")
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,book):
        try:
            if book in Book:
                self._book=book
        
        except:("Author must be an instance of author")

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,date):        
        try:
             if isinstance(date,str):
                 self._date=date
        except:("Date must be  string")
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,royalty):        
        try:
             if isinstance(royalty,int):
                 self._royalties=royalty
        except:("Royalty must be  an integer")
    
    @classmethod
    def contracts_by_date(cls,date):
        if isinstance(date,cls.date):
            return cls.my_contracts

        
        
                
                
        
        
            
    

        