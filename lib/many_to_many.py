# class Author:
#     all=[]
#     def __init__(self,name):
#         if isinstance(name,str):      
#             self.name=name
#         else:raise ValueError("Name must be a string")
#         self._contracts=[]
#         Author.all.append(self)
    
#     def books(self):    
#        return [contract.book for contract in Contract.all if contract.author==self]
    
#     def sign_contract(self,book,date,royalties):
#         if not isinstance(book,Book):
#             raise ValueError("Book must be an instance of a book")
#         if not isinstance(royalties,int):
#             raise ValueError("Royalties must be an integer")
#         if not isinstance(date,str):
#             raise ValueError("Date must be a string")
#         contract=Contract(self,book,date,royalties)
#         return contract
     
#     def contracts(self):
#         #return [all_contracts for all_contracts in Contract.my_contracts  if Contract.author==self.name]
#          return [contract for contract in Contract.all if contract.author==self]

#     def total_royalties(self):
#         # all_royalties=0
#         # for contracts in Contract.my_contracts :
#         #   if Contract.author==self:
#         #    all_royalties+=contracts.royalties
#         return sum(contract.royalties for contract in Contract.all if contract.author==self)

# class Book:
#     all=[]
#     def __init__(self,title):
#         if isinstance(title,str):
#           self.title=title
#         else:raise ValueError("The title must be a string")
#         Book.all.append(self)

#     def books(self):
#         return self.all

#     def authors(self):
#         # for author in Author.contracts:
#         #  if isinstance(self.title,author.title):
#         #    return author.name 
#         return [contract.author for contract in Contract.all if contract.book==self]
    
#     def contracts(self):
#        return [contract for contract in Contract.all if contract.book==self]
    
# class Contract:
#     all=[]
#     def __init__(self,author,book,date,royalties):
#         if isinstance(author,Author):
#             self.author=author
#         else:raise Exception("Author must be an instance of author")
       
#         if isinstance(book,Book):
#             self._book=book
#         else:raise Exception("Book must be an instance of book class")
#         #self._book=book
#         if isinstance(date,str):
#             self.date=date
#         else:raise Exception("Date must be  string")
#         if isinstance(royalties,int):
#             self.royalties=royalties
#         else:raise Exception("Royalties must be a string")
#         self.all.append(self)    
#         #Contract.contract_by_date(date)
#     @property
#     def author(self):
#         return self._author
    
#     @author.setter
#     def author(self,author):     

#                if isinstance(author,Author):
#                 self._author=author
        
#                else:raise Exception("Author must be an instance of author")
    
#     @property
#     def book(self):
#         return self._book
    
#     @book.setter
#     def book(self,book):
#         try:
#             if book in Book:
#                 self._book=book
        
#         except:("Author must be an instance of author")

#     @property
#     def date(self):
#         return self._date
    
#     @date.setter
#     def date(self,date):        
#         try:
#              if isinstance(date,str):
#                  self._date=date
#         except:("Date must be  string")
    
#     @property
#     def royalties(self):
#         return self._royalties
    
#     @royalties.setter
#     def royalties(self,royalty):        
#         try:
#              if isinstance(royalty,int):
#                  self._royalties=royalty
#         except:("Royalty must be  an integer")
    
#     @classmethod
#     def contracts_by_date(cls,date):        
#             return [contracts for contracts in Contract.all if contracts.date==date]

class Book:
    all=[]
    def __init__(self,title) :
        if isinstance(title,str):
         self.title=title 
        else:raise ValueError("Title should be a string")
        self.all.append(self)

    def contracts(self):
        all_contracts=[contract for contract in Contract.all if contract.book==self]
        return all_contracts
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book==self]
class  Author:
    all=[]    
    def __init__(self,name) :
        if isinstance(name,str):
          self.name=name
        else:raise ValueError("Author name should be a string")
        self._contracts=[]
        self.all.append(self)

    def contracts(self):
        all_contracts=[contract for contract in Contract.all if contract.author==self]
        return all_contracts
    
    def books(self):
        all_books=[contract.book for contract in Contract.all if contract.author==self]
        return all_books
    
    def sign_contract(self,book,date,royalties):
        if not isinstance(book,Book):
            raise ValueError("Book must be an instance of a book")
        if not isinstance(royalties,int):
            raise ValueError("Royalties must be an integer")
        if not isinstance(date,str):
            raise ValueError("Date must be a string")
        new_contract=Contract(self,book,date,royalties)
        self._contracts.append(new_contract)
        return new_contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in Contract.all if contract.author==self)
class Contract:
    all=[]
    def __init__(self,author,book,date,royalties):
        if isinstance(author,Author):
            self.author=author
        else:raise ValueError("Auhtor should be an instance of the author class")
        if isinstance(book,Book):
            self.book=book
        else:raise ValueError("book must be an instance of the book class")
        if isinstance(date,str):
            self.date=date
        else:raise ValueError("Date should be a string")
        if isinstance(royalties,int):
            self.royalties=royalties
        else:raise ValueError("Royalties should be a string")
        self.all.append(self)
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in Contract.all if contract.date==date]
        


        
                
                
        
        
            
    

        