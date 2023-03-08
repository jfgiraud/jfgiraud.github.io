---
title: "java, mockito espionner le retour d'une fonction"
date: "2016-02-18 09:42:00"
tags: java test tu
---
Le code n'est pas beau, mais au moins il est copiable directement en test unitaire pour manipuler et tester !


```java
    @Test
    public void testFoo() throws Exception {
        class ResultCaptor implements Answer<String> {
            private String result;

            String getResult() { return result; }

            @Override
            public String answer(InvocationOnMock invocationOnMock) throws Throwable {
                result = (String) invocationOnMock.callRealMethod();
                return result;
            }
        }

        class MyClazz {
            public String f(String param) { return "out=" + param; }
        }

        MyClazz a = new MyClazz();
        MyClazz spy = spy(a);

        ResultCaptor answer = new ResultCaptor();
        when(spy.f(anyString())).thenAnswer(answer);

        class ClazzUsingMyClass {
            private final MyClazz myClazz;

            public ClazzUsingMyClass(MyClazz clazz) {
                this.myClazz = clazz;
            }

            public void g() {
                String t = myClazz.f("hello");
                System.out.println(t);
            }
        }

        ClazzUsingMyClass usingMyClass = new ClazzUsingMyClass(spy);

        usingMyClass.g();

        assertThat(answer.getResult()).isEqualTo("out=hello");
    }
```
