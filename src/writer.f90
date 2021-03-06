module writer_mod

implicit none

    contains
        subroutine writer(w, xmax, ymax, zmax, nphotons, numproc)

            use constants, only : nxg,nyg,nzg,fileplace
            use iarray,    only : jmeanGLOBAL, albedoar, rhokap
            use photon_vars, only : d_nzg, e_nzg, m_nzg, b_nzg, sc_nzg, h_nzg
            use iso_fortran_env, only: int64

            implicit none
            
            integer(kind=int64) :: nphotons

            integer           :: i, u, numproc, j,k, w
            real              :: xmax, ymax, zmax, jm(nzg)
            character(len=10) :: file_id
            character(len=50) :: file_name
            logical :: exist
             character(len=70) :: fn
    !integer, parameter :: numfiles=40
            
            
            
!normalise the fluence rate  - different loops for each resolution

           do i = 1, nxg

                 do j = 1, nyg

                do k=1,300 !30 um sc
                        !do k = 1, 200 !20um sc
                !do k= 1,150 !15um sc
                !do k= 1,100 !10um sc
                !comment out this do loop for 0um sc

                  jmeanGLOBAL(i,j,k) =jmeanGLOBAL(i,j,k) *((2.*xmax)**2./(nphotons*numproc*(2.*xmax/nxg) &
                                *(2.*ymax/nyg)*(2.*zmax/sc_nzg)))

                                !print*, jmeanGLOBAL(i,j,k), i,j,k

                         end do
                end do
           end do

             do i = 1, nxg

                 do j = 1, nyg

                do k= 301,400 !30um sc
                        !do k = 201, 300 !20um sc
                !do k= 151,250 !15um sc
                !do k= 101,200 !10um sc
                !do k= 1,100 !0um sc
                  jmeanGLOBAL(i,j,k) =jmeanGLOBAL(i,j,k) *((2.*xmax)**2./(nphotons*numproc*(2.*xmax/nxg) &
                                *(2.*ymax/nyg)*(2.*zmax/e_nzg)))
                         end do
                end do
           end do

              do i = 1, nxg

                 do j = 1, nyg

                do k= 401,500 !30 um sc
                        !do k = 301, 400 !20um sc
                !do k= 251,350 !15um sc
                !do k=201,300 !10um sc
                !do k= 101,200 !0um sc
                 jmeanGLOBAL(i,j,k) =jmeanGLOBAL(i,j,k) *((2.*xmax)**2./(nphotons*numproc*(2.*xmax/nxg) &
                                *(2.*ymax/nyg)*(2.*zmax/m_nzg)))
                         end do
                end do
           end do

             do i = 1, nxg

                 do j = 1, nyg

                do k= 501, 600 !30um sc
                        !do k = 401, 500 !20um sc
                !do k= 351,450 !15um sc
                !do k= 301, 400 !10um sc
                !do k=201,300 !0um sc
                 jmeanGLOBAL(i,j,k) =jmeanGLOBAL(i,j,k) *((2.*xmax)**2./(nphotons*numproc*(2.*xmax/nxg) &
                                *(2.*ymax/nyg)*(2.*zmax/b_nzg)))
                         end do
                end do
           end do

            do i = 1, nxg

                 do j = 1, nyg

                do k= 601,750 !30um sc
                        !do k = 501, 650 !20um sc
                !do k= 451, 600 !15um sc
                !do k=401, 550 !10um sc
                !do k=301,450 !0um sc
                 jmeanGLOBAL(i,j,k) =jmeanGLOBAL(i,j,k) *((2.*xmax)**2./(nphotons*numproc*(2.*xmax/nxg) &
                                *(2.*ymax/nyg)*(2.*zmax/d_nzg)))
                         end do
                end do
           end do

           do i = 1, nxg

                 do j = 1, nyg

                do k=751,900 !30um sc
                        !do k = 651, 800 !20um sc
                !do k= 601,750 !15um sc
                !do k= 551,700 !10um sc
                !do k= 451,600 !0um sc
                 jmeanGLOBAL(i,j,k) =jmeanGLOBAL(i,j,k) *((2.*xmax)**2./(nphotons*numproc*(2.*xmax/nxg) &
                                *(2.*ymax/nyg)*(2.*zmax/h_nzg)))
                         end do
                end do
           end do



          
           

            !jmeanGLOBAL =jmeanGLOBAL * ((2.*xmax)**2./(nphotons*numproc*(2.*xmax/nxg)*(2.*ymax/nyg)*(2.*zmax/nzg)))

            inquire(iolength=i)jmeanGLOBAL

           ! open(newunit=u,file=trim(fileplace)//'jmean400.dat',access='stream',status='REPLACE',form='unformatted')
            !write(u) jmeanGLOBAL
            !close(u)
            
            !open(newunit=u,file=trim(fileplace)//'rhokap.dat',access='stream',status='REPLACE',form='unformatted')
            !write(u) rhokap
            !close(u)
            
         ! build filename -- i.dat
        write(fn,fmt='(i0,a)') w, 'jmean_direct_30umsc.dat'

        ! open it with a fixed unit number
        open(newunit=u,file=trim(fileplace)//fn, status="replace", access='stream', form='unformatted')

        ! write something
        write(u) jmeanGLOBAL

        ! close it 
        close(u)
            
         
            
            

           ! jm = 0.d0
            !do k = 1, nzg
                !do j = 1, nyg
                   ! do i = 1, nxg
                    !    jm(k) = jm(k) + jmeanGLOBAL(i,j,k)
                    !end do
                !end do
            !end do

            !jm = jm / (nxg*nyg)

            !open(newunit=u,file=trim(fileplace)//"jmean/validation-350-full_sc.dat",status="replace")
            !do i = nzg,1,-1
                !write(u,*)real(nzg-i)*(2./nzg),jm(i)
           ! end do
            !close(u)
        end subroutine writer
end module writer_mod
